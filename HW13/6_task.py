"""Задание №task_6
    📌 На семинаре 13 был создан проект по работе с
       пользователями (имя, id, уровень).
    📌 Напишите 3-7 тестов pytest для данного проекта.
    📌 Используйте фикстуры."""
import pytest
from pathlib import Path
from Seminar.lesson_13.task_6 import User, ErrorLevel

path_res_user = Path("/Users/sergey/PycharmProjects/pythonProject/"
                     "Погружение_в_Python/Dive_into_Python/"
                     "Seminar/lesson_13/users2.json")


@pytest.fixture
def fix():
    user = User('Карина', 18, 3)
    user.json_read(path_res_user)
    return user


def test_1(fix):
    assert fix.log_id('Карина', 11111) == 3


def test_2(fix):
    with pytest.raises(ErrorLevel, match='Уровень доступа не достаточен'):
        fix.creat_new_user('Инна', 7)


if __name__ == '__main__':
    pytest.main(['-v'])