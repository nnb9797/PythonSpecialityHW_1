"""Задача №task_6 семинара 14.
На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта. Используйте фикстуры."""

import json

import pytest

from task_4 import UserData
from task_5 import Project
from task_6 import MyAccessEx, MyLevelEx


FILE = 'ex1.json'


@pytest.fixture
def users_data():
    new_data = {
        UserData('Нео', 100, 1),
        UserData('Дипси', 101, 2),
        UserData('Котопёс', 102, 2),
        UserData('Дамбо', 103, 3),
    }
    return new_data


@pytest.fixture
def high_level_user():
    return UserData('Нео', 100, 1)


@pytest.fixture
def new_low_level_user():
    return UserData('Максим', 105, 5)


def test_load_json(users_data):
    """Тестирование загрузки данных из файла json"""
    data = {
        1: {100: 'Нео'},
        2: {101: 'Дипси', 102: 'Котопёс'},
        3: {103: 'Дамбо'}
    }
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    project1 = Project()
    test_result = project1.load_json(FILE)
    assert test_result == users_data


def test_enter_valid_user(high_level_user):
    """Тестирование входа в систему существующего пользователя"""
    new_pr = Project()
    new_pr.load_json(FILE)
    test_user = new_pr.enter('Нео', 100)
    assert test_user == high_level_user


def test_enter_invalid_user():
    """Тестирование входа в систему несуществующего пользователя"""
    new_pr = Project()
    new_pr.load_json(FILE)
    with pytest.raises(MyAccessEx, match=r'Пользователя с именем Максим и id 105 нет в системе! Доступ запрещён!'):
        new_pr.enter('Максим', 105)


def test_add_lower_level_user(new_low_level_user):
    """Тестирование добавления пользователя с более низким уровнем, чем у администратора"""
    new_pr = Project()
    new_pr.load_json(FILE)
    new_pr.enter('Нео', 100)
    new_user = new_pr.add_user('Максим', 105, 5)
    assert new_user == new_low_level_user


def test_add_higher_level_user():
    """Тестирование добавления пользователя с более высоким уровнем, чем у администратора"""
    new_pr = Project()
    new_pr.load_json(FILE)
    new_pr.enter('Дамбо', 103)
    with pytest.raises(MyLevelEx, match=r'Уровень доступа пользователя Василий Иванович - 1 '
                                        r'ниже уровня доступа администратора 3! Доступ запрещён!'):
        new_pr.add_user('Василий Иванович', 104, 1)


if __name__ == '__main__':
    pytest.main(['-vv'])
   