# ------------------------------------------- 3 -----------------------------
"""
📌 Создайте класс с базовым исключением и дочерние классы-исключения:
    ○ ошибка уровня,
    ○ ошибка доступа.
"""


class CustomException(Exception):
    pass


class LevelError(CustomException):
    pass


class AccessError(CustomException):
    pass


try:
    raise LevelError("Произошла ошибка уровня!")
except LevelError as le:
    print("Поймано исключение уровня:", le)

try:
    raise AccessError("Произошла ошибка доступа!")
except AccessError as ae:
    print("Поймано исключение доступа:", ae)
