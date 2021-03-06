# -*- coding: utf-8 -*-

import view
from config import *
from models import Team
from datetime import datetime
from exception_guard import exception_guard


@exception_guard
def add_team(chat_id, name, part_count, section):
    team = Team.create(
        chat_id=chat_id,
        name=name,
        participants=part_count,
        section=section)
    return team


@exception_guard
def set_section(chat_id, section):
    query = (Team.update({Team.section: section}).where(Team.chat_id == chat_id))
    query.execute()
    return SUCCESS


@exception_guard
def get_team(chat_id):
    return Team.get(Team.chat_id == chat_id)


@exception_guard
def get_all_teams():
    return (Team.select())


@exception_guard
def flush_team_status():
    query = (Team.update({Team.status: OFFLINE_GAME_OFF, Team.off_score: 0}))
    query.execute()
    return SUCCESS


@exception_guard
def set_team_responding(chat_id):
    query = (Team.update({Team.responding: True}).where(Team.chat_id == chat_id))
    query.execute()


@exception_guard
def is_team_responding(chat_id):
    return get_team(chat_id).responding


@exception_guard
def get_section(chat_id):
    return get_team(chat_id).section


@exception_guard
def next_online_level(chat_id, skipped=False):
    team = get_team(chat_id)
    point = view.point.get_point(team.on_point)
    score = team.on_score
    if not skipped:
        score += max(point.score - point.score / point.attempts * team.attempt_num, 0)
    new_point_num = point.id + 1
    if point.name == LAST_POINT_NAME:
        status = ONLINE_GAME_OVER
    else:
        status = team.status
    query = (Team
             .update({Team.on_score: score,
                      Team.on_point: new_point_num,
                      Team.attempt_num: 0,
                      Team.status: status})
             .where(Team.chat_id == chat_id))
    query.execute()


@exception_guard
def next_offline_level(chat_id):
    team = get_team(chat_id)
    point = view.point.get_point(team.off_point, team.section)
    score = team.off_score + max(point.score - point.score / OFFLINE_POINT_ATTEMPTS * team.attempt_num, 0)
    new_point_num = point.id + 1
    if point.name == LAST_POINT_NAME:
        status = OFFLINE_GAME_OVER
    else:
        status = team.status
    query = (Team
             .update({Team.off_score: score,
                      Team.off_point: new_point_num,
                      Team.attempt_num: 0,
                      Team.responding: False,
                      Team.status: status})
             .where(Team.chat_id == chat_id))
    query.execute()


@exception_guard
def is_finished(chat_id):
    if MODE == ONLINE:
        game_over = ONLINE_GAME_OVER
    else:
        game_over = OFFLINE_GAME_OVER
    return get_team(chat_id).status == game_over


@exception_guard
def is_running(chat_id):
    if MODE == ONLINE:
        run = ONLINE_GAME_ON
    else:
        run = OFFLINE_GAME_ON
    return get_team(chat_id).status == run


@exception_guard
def on_game_start(chat_id):
    query = (Team
             .update({Team.on_point: 1, Team.status: ONLINE_GAME_ON})
             .where(Team.chat_id == chat_id))
    query.execute()


@exception_guard
def off_game_start(chat_id):
    query = (Team
             .update({Team.off_point: 1, Team.status: OFFLINE_GAME_ON})
             .where(Team.chat_id == chat_id))
    query.execute()


@exception_guard
def set_wrong(chat_id):
    if MODE == ONLINE:
        next_level = next_online_level
        resp = False
    else:
        next_level = next_offline_level
        resp = True
    if attempt_was_last(chat_id):
        next_level(chat_id)
        return ATTEMPT_WAS_LAST
    else:
        query = (Team
                 .update({Team.attempt_num: Team.attempt_num + 1, Team.responding: resp})
                 .where(Team.chat_id == chat_id))
        query.execute()
        return ATTEMPT_WAS_NOT_LAST


@exception_guard
def attempt_was_last(chat_id):
    team = get_team(chat_id)
    if MODE == ONLINE:
        attempts = view.point.get_point(team.on_point).attempts
    else:
        attempts = OFFLINE_POINT_ATTEMPTS
    return team.attempt_num + 1 == attempts


@exception_guard
def set_cur_time(chat_id):
    query = (Team.update({Team.cur_start_time: datetime.now()}).where(Team.chat_id == chat_id))
    query.execute()


@exception_guard
def change_bot_reaction(chat_id, mode):
    query = (Team.update({Team.bot_reaction: mode }).where(Team.chat_id == chat_id))
    query.execute()


@exception_guard
def is_bot_speaking(chat_id):
    return get_team(chat_id).bot_reaction


@exception_guard
def delete_team(chat_id):
    team = get_team(chat_id)
    team.delete_instance()
    return SUCCESS
