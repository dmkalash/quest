# -*- coding: utf-8 -*-

from peewee import *
from config import *
from db_utils.db_init import database


class BaseModel(Model):
    class Meta:
        database = database
        order_by = ('created_at',)


class OnPoint(BaseModel):
    """
    Online Point - Point for online quest mode.
        id: Point number in order of completion. The first Point has id 0. The first and last points are just plugs
        name: Point's name by the scenario
        task: Text of task
        score: score that team getting after completing the task without mistakes
        attempts: Attempts count for current Point
        right_answer: right answer for current task
        artifacts: artifacts count for completing
    """
    id = IntegerField(unique=True)
    name = TextField()
    task = TextField()
    score = IntegerField()
    attempts = IntegerField()
    right_answer = TextField()
    artifacts = IntegerField()


class OffPoint(BaseModel):
    """
    Offline Point - Point for offline quest mode.
        id: Point number in order of completion. The first Point has id 0. The first and last points are just plugs
        name: Point's name by the scenario
        start_code: check-in code for current point
        finish_code: check-out code for current point
        task: Text of task
        score: score that team getting after completing the task without mistakes
        section: section point number for dividing in offline part
        fast: time(in minutes) for completing point in good case
        middle: time(in minutes) for completing point in middle case
        slow: time(in minutes) for completing point in bad case
    """
    id = IntegerField()
    section = IntegerField()
    name = TextField()
    start_code = TextField(unique=True)
    finish_code = TextField(unique=True)
    task = TextField()
    score = IntegerField()
    fast = IntegerField()
    middle = IntegerField()
    slow = IntegerField()


class Team(BaseModel):
    """
    Model for team.
        chat_id: telegram chat id
        name: team name
        participants: count of participants
        on_score: current score for online-mode game
        off_score: current score for offline-mode game
        on_point: current number of online-point
        off_point: current number of offline-point
        attempt_num: current point completing attempt number
        artifacts: count of artifacts
        status: game status of the team
        section: section team number for dividing teams in offline part
        cur_start_time: start date-time of current offline-mode point
        bot_reaction: users' plain text bot reactions(ON/OFF)
        responding: Flag if team is responding for a task
    """
    chat_id = IntegerField(unique=True)
    name = TextField()
    participants = IntegerField()
    on_score = IntegerField(default=0)
    off_score = IntegerField(default=0)
    on_point = IntegerField(default=0)
    off_point = IntegerField(default=0)
    attempt_num = IntegerField(default=0)
    artifacts = IntegerField(default=0)
    status = IntegerField(default=ONLINE_GAME_OFF)
    section = IntegerField(default=0)
    cur_start_time = DateTimeField(null=True)
    bot_reaction = BooleanField(default=True)
    responding = BooleanField(default=False)


class OffReaction(BaseModel):
    """
    Message as reaction on some user actions. For offline mode.
        text: Text of reaction
        point_num: point that current reaction applies to
        order_num: number in order.
                1 - RIGHT_ANSWER
                2 - WRONG_ANSWER
                3 - LOSE
    """
    id = AutoField()
    text = TextField()
    point_num = IntegerField()
    order_num = IntegerField()


class OnReaction(BaseModel):
    """
    Message as reaction on some user actions. For online mode.
        text: Text of reaction
        point_num: number of point that current reaction applies to
        order_num: number in order.
                1 - RIGHT_ANSWER
                2 - WRONG_ANSWER
                3 - LOSE
    """
    id = AutoField()
    text = TextField()
    point_num = IntegerField()
    order_num = IntegerField()


class File(BaseModel):
    """
    File Model.
        file_id: telegram file id
        point: Point that current file applies to
        order_num: file number in order
        file_type: type of file
    """
    id = AutoField()
    file_id = TextField()
    point = ForeignKeyField(OnPoint, backref='file_point')
    order_num = IntegerField()
    file_type = IntegerField()
