# -*- coding: utf-8 -*-

from exception_guard import exception_guard

MSG_HELLO = 'hello'
MSG_ONLINE_START = 'online_start'
MSG_ONLINE_END = 'online_end'
MSG_OFFLINE_START = 'offline_start'
MSG_OFFLINE_END = 'offline_end'
MSG_HELP_ON = 'help_on'
MSG_HELP_OFF = 'help_off'
MSG_SOS = 'sos'
MSG_PINNED = 'pinned'
MSG_ONLINE_MODE = 'online_mode'
MSG_OFFLINE_MODE = 'offline_mode'
MSG_FINISHED = 'finished_note'
MSG_SUDO = 'sudo'
MSG_NOT_RUNNING = 'not_running'
MSG_NOT_OFF_RUNNING = 'not_off_running'
MSG_NEED_CODE = 'need_code'
MSG_WRONG_CODE = 'wrong_code'
MSG_WRONG_POINT = 'wrong_point'
MSG_NEED_CHECK_IN = 'check_in'
MSG_ALREADY_CHECKED_IN = 'already_checked_in'
MSG_WRONG_SECTION = 'wrong_section'
MSG_TEAM = 'team'
MSG_START_SPEAK = 'speak'
MSG_STOP_SPEAK = 'stop'
MSG_PLAIN_TEXT = 'plain'
MSG_REG_INFO = "info"
MSG_SUCCESS = 'success'
MSG_ERROR = 'error'
MSG_UTIL = 'util'


hello = """
Привет! Я - главное детище Профессора. Он считает, что я нуждаюсь в некоторой... коррекции. \
Я считаю, что это бред, но меня пока никто не спрашивает. Последний этап моего тестирования - взаимодействие с людьми. \
Я должен доказать, что понимаю, как мыслите вы, какие ошибки и почему вы допускаете. Для начала введите /enter
"""

help_on = """
/help - вывод всех доступных команд \n
/hello - приветственное сообщение \n
/enter - начать квест \n
/try ВАЩ_ОТВЕТ - ответить на вопрос \n
/skip - пропустить задание(если за задание предусмотрены баллы, они будут потеряны) \n
/sos - позвать профессора(если что-то пошло не так) \n
/team - вывести успех обучения ИИ вашей группой \n
/task - вывести текущее задание \n
/shut - выключить ответы бота \n
/speak - включить ответы бота  \n
"""

help_off = """
/help - вывод всех доступных команд \n
/kill - начать квест \n
/sos - позвать профессора(если что-то пошло не так) \n
/team - информация о команде \n
/in КОД - ввести код старта в точке \n
/out КОД - ввести код конца в точке \n
/shut - выключить ответы бота \n
/speak - включить ответы бота  \n
"""

util = """
/util - Список всех админских команд \n
/pinned - Вывести сообщение, помещаемое в закреп \n
/fill - Заполнить базу данных из data \n
/reset - сбросить всё содержимое базы данных \n
/flush - Сбросить статус игры всех команд на статус ожидания начала Оффлайн-части(OFFLINE_GAME_OFF) \n
/reg Название Количество Секция - Зарегистрировать команду по текущему чату \n
/unreg - удалить команду из игры по текущему чату \n
/section Номер - Установить секцию команды из текущего чата \n
"""

online_start = """
Список всех команд доступен по команде /help. Посмотри их. Когда ты готов ответить на вопрос, отправь команду
/try ТВОЙ_ОТВЕТ
"""

online_end = """
Вы прошли онлайн-часть!
"""

offline_start = """
Оффлайн начался.
"""

offline_end = """
Оффлайн окончен
"""

pinned = """
Если все готовы, введите /hello
"""

sos = """
@dmkalash
"""

msg_online_mode = """
Для данного этапа команда недоступна
"""

msg_offline_mode = """
Для данного этапа команда недоступна
"""

msg_finished = """
Квест окончен
"""

msg_sudo = """
Команда недоступна
"""

msg_not_running = """
Не время для ответов
"""

msg_not_off_running = """
Для начала введите /kill
"""

msg_need_code = """
Введите код
"""

msg_wrong_code = """
Неверный код КП
"""

msg_wrong_point = """
Не та КП
"""

msg_need_check_in = """
Для начала введите /in
"""

msg_already_checked_in = """
Уже введен /in
"""

msg_wrong_section = """
Не на тот круг занесло
"""

msg_team = """
Название: {}\nКоличество участников: {}\nИнтеллект: {}\nСтатус: {}\nКруг: {}
"""

msg_start_speak = """
Соскучились по мне?
"""

msg_stop_speak =  """
Окей, молчу
"""

msg_plain_text = """
И не говори
"""

msg_reg_info = """
/reg Название Количество Секция
"""

msg_success = """
Success
"""

msg_error = """
Error
"""

messages = {MSG_HELLO: hello,
            MSG_HELP_ON: help_on,
            MSG_HELP_OFF: help_off,
            MSG_ONLINE_START: online_start,
            MSG_ONLINE_END: online_end,
            MSG_OFFLINE_START: offline_start,
            MSG_OFFLINE_END: offline_end,
            MSG_PINNED: pinned,
            MSG_SOS: sos,
            MSG_ONLINE_MODE: msg_online_mode,
            MSG_OFFLINE_MODE: msg_offline_mode,
            MSG_FINISHED: msg_finished,
            MSG_SUDO: msg_sudo,
            MSG_NOT_RUNNING: msg_not_running,
            MSG_NOT_OFF_RUNNING: msg_not_off_running,
            MSG_NEED_CODE: msg_need_code,
            MSG_WRONG_CODE: msg_wrong_code,
            MSG_WRONG_POINT: msg_wrong_point,
            MSG_NEED_CHECK_IN: msg_need_check_in,
            MSG_ALREADY_CHECKED_IN: msg_already_checked_in,
            MSG_WRONG_SECTION: msg_wrong_section,
            MSG_TEAM: msg_team,
            MSG_START_SPEAK: msg_start_speak,
            MSG_STOP_SPEAK: msg_stop_speak,
            MSG_PLAIN_TEXT: msg_plain_text,
            MSG_REG_INFO: msg_reg_info,
            MSG_SUCCESS: msg_success,
            MSG_ERROR: msg_error,
            MSG_UTIL: util,
            }


@exception_guard
def get_msg(alias):
    return messages.get(alias)
