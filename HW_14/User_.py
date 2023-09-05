"""Задание №task_6
    📌 Доработайте классы исключения так, чтобы они выдали
       подробную информацию об ошибках.
    📌 Передавайте необходимые данные из основного кода
       проекта."""
import json


class User:
    def __init__(self, name: str, user_id: str,  level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __repr__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __hash__(self):                                     # при переопределениии eq надо переопределять hash
        return hash(self.name) + hash(self.user_id)

    def __eq__(self, other):                                                           # True/False в зависимоти от выполнения условий
        return self.name == other.name and self.user_id == other.user_id

class BaseExeption(Exception):
    pass

class LevelError(BaseExeption):
    def __init__(self, value, value_min):
        self.value = value
        self.value_min = value_min

    def __str__(self):
        return f"Ошибка уровня - {self.value} > минимального уровня {self.value_min}"

class AccesErorr(BaseExeption):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return f"Ошибка доступа - {self.value}"

class AccesErorr(BaseExeption):

    def __str__(self):
        return f"Ошибка доступа "




def fun(num):
    if num < 2:
        raise AccesErorr
    elif num > 5:
        raise LevelError
    else:
        print('все ок')


if __name__ == '__main__':
    raise LevelError(4, 1)
    fun(1)
if __name__ == '__main__':

    work_group = set()

    def load_users(path: str = 'users2.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                work_group.add(User(name, id, level))           # создали объекты User и записали во множество


    load_users()
    print(work_group)