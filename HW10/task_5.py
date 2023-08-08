# 5. Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.


class Animals:
    def __init__(self, name):
        self.name = name

    def animal_name(self):
        return f'Имя: {self.name}'

class Fish(Animals):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_info(self):
        return f'Глубина обитания: {self.depth} м '

class Birds(Animals):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def get_info(self):
        return f'Размах крыльев: {self.wingspan} м '

class Reptile(Animals):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_info(self):
        return f'Максимальный возраст: {self.age} л '

class Amphibia(Animals):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def get_info(self):
        return f'Средний вес: {self.weight} кг '


if __name__ == '__main__':
    fish = Fish('Тигровая акула', 350)
    bird = Birds('Альбатрос', 3)
    reptile = Reptile('Черепаха', 150)
    amphibia = Amphibia('Лягушка Голиаф', 5)
    print(fish.animal_name())
    print(fish.get_info())
    print(bird.animal_name())
    print(bird.get_info())
    print(reptile.animal_name())
    print(reptile.get_info())
    print(amphibia.animal_name())
    print(amphibia.get_info())
