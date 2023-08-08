# 4.Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления суммы цифр id на семь


from random import randint


class Human:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Employee(Human):

    def __init__(self, first_name, last_name, age, id_num):

        super().__init__(first_name, last_name, age)
        if (99999 < id_num) and (id_num < 10000000):
            self.id_num = id_num
        else:
            self.id_num = randint(100000, 999999)

    def set_level(self):
        return sum([int(item) for item in str(self.id_num)]) % 7


if __name__ == '__main__':
    spam = Employee('Smit', 'Jon', 33, 89)
    print(f'{spam.id_num = }')
    print(f'{spam.set_level() = }')
