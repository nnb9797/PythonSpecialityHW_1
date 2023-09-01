# ------------------------------------------- 4 -----------------------------
"""
📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
   где в бесконечном цикле запрашивали имя, личный
   идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию
   из JSON файла и формирует множество пользователей.
"""

import json


class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level

    def to_dict(self):
        return {"name": self.name, "id": self.id, "access_level": self.access_level}

    def __str__(self):
        return f"User(name={self.name}, id={self.id}, access_level={self.access_level})"


def save_to_json(users):
    user_data = [user.to_dict() for user in users]
    with open("users.json", "w") as file:
        json.dump(user_data, file, indent=4)


def read_from_json():
    users = []
    try:
        with open("users.json", "r") as file:
            user_data = json.load(file)
            for user_info in user_data:
                users.append(User(user_info["name"], user_info["id"], user_info["access_level"]))
    except FileNotFoundError:
        pass
    return users


users = []

while True:
    name = input("Введите имя пользователя (или 'exit' для завершения): ")
    if name == 'exit':
        break
    id = input("Введите личный идентификатор: ")
    access_level = int(input("Введите уровень доступа (от 1 до 7): "))
    users.append(User(name, id, access_level))

save_to_json(users)
print("Данные сохранены в users.json")

loaded_users = read_from_json()
print("Загруженные пользователи:")
for user in loaded_users:
    print(user)
