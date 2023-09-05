# Доработаем задачи 5-task_6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики


class AnimalFactory:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return (f'{"Class:":8}{type(self).__name__}'
                f'\n{"Name:":8}{self.name}'
                f'\n{"Age:":8}{self.age} years')


class Mammal(AnimalFactory):

    def __init__(self, name: str, age: int, hair: str, voice: str):
        super().__init__(name, age)
        self.hair = hair
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Hair:":8}{self.hair}'
                f'\n{"Voice:":8}{self.voice}\n'
                )


class Bird(AnimalFactory):

    def __init__(self, name: str, age: int, color: str, voice: str):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}'
                f'\n{"Voice:":8}{self.voice}\n'
                )


bird = Bird('Альбатрос', 20, 'черно-белый', 'кра')
print(f'{bird.name = }, \n{bird.age = }, \n{bird.voice = }, \n{bird.color = }, \n{bird.get_info()}')
