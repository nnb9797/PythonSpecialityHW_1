# task_6.Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animals:
    def __init__(self, name, weight):
        self.__name, self.__age = name, weight

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

class Fish(Animals):

    def __init__(self, name, age, depth):
        super().__init__(name, age)
        self.__name, self.__age = age, depth
        self.__depth = depth

    def get_specific(self):
        return self.__depth

class Reptile(Animals):

    def __init__(self, name, age, shell):
        super().__init__(name, age)
        self.__name, self.__age = age, shell
        self.__shell = shell

    def get_specific(self):
        return self.__shell

class Bird(Animals):

    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.__name, self.__age = age, wingspan
        self.__wingspan = wingspan

    def get_specific(self):
        return self.__wingspan


class Amphibia(Animals):

    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.__name, self.__age = age, weight
        self.__weight = weight

    def get_specific(self):
        return self.__weight


if __name__ == '__main__':
    bird = Bird("Альбатрос", "20", "3")
    print(f'название: {bird.get_name()}, средний возраст: {bird.get_age()} л, размах крыльев: {bird.get_specific()} м')
    fish = Fish("Акула", "70", "350")
    print(f'название: {fish.get_name()}, средний возраст: {fish.get_age()} л, глубина обитания: {fish.get_specific()} м')
    amphibia = Amphibia("Лягушка", "7", "5")
    print(f'название: {amphibia.get_name()}, средний возраст: {amphibia.get_age()} л, '
          f'средний вес: {amphibia.get_specific()} кг')
    reptile = Reptile("Черепаха", "350", "панцирь")
    print(f'название: {reptile.get_name()}, средний возраст: {reptile.get_age()} л, '
          f'покров: {reptile.get_specific()}')