# Создайте класс с базовым исключением и дочерние классы-исключения:
# ошибка уровня,
# ошибка доступа.
# Вспомните задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7).
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Реализуйте магический метод проверки на равенство пользователей

from dataclasses import dataclass


@dataclass
class User:

    name: str
    id_: int
    level: int = None

    def __eq__(self, other):
        """Users comparison by name and id"""
        return  self.id_ == other.id_ and self.name == other.name

if __name__ == "__main__":
    e1 = User('asd', 5, 6)
    e2 = User('asd', 3, 6)
    print(e1.level > e2.level)