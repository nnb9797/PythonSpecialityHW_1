# 6. Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.


class Validator:
    """Дескриптор с валидацией размера."""
    def __init__(self, min_value: float = None, max_value: float = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{value} меньше, чем {self.min_value}!')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{value} больше, чем {self.max_value}!')


class Rectangle:
    """Ограничение ширины для вычисления прямоугольника через класс Validator."""
    width = Validator(1, 100)
    length = Validator(1, 200)

    def __init__(self, width: float, length: float = None) -> None:
        self.width = width
        self.length = length if length else width

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def get_area(self) -> float:
        return self.width * self.length

    def __str__(self):
        return f'Rectangle({self.width}, {self.length})' \
               f'\nPerimetr {self.get_perimeter()}' \
               f'\nArea {self.get_area()}'

    def __repr__(self):
        return f'Rectangle({self.width, self.length})'

def main():
    rect = Rectangle(10, 20)
    print(rect.__str__())

    rect = Rectangle(10, 10)
    print(f'{rect=}')
    print(rect.__str__())

    some_rect = Rectangle(10, 20)
    print(f'{some_rect=}')
    some_rect.length = 200
    some_rect.width = 100
    print(f'{some_rect=}')
    try:
        some_rect.length = 300
    except Exception as exc:
        print(f'{exc.__class__.__name__}:{exc}')
    try:
        some_rect.width = -100
    except Exception as exc:
        print(f'{exc.__class__.__name__}:{exc}')
    print(f'{some_rect=}')
    try:
        some_rect.length = 0.91
    except Exception as exc:
        print(f'{exc.__class__.__name__}:{exc}')
    try:
        some_rect.width = 0.55
    except Exception as exc:
        print(f'{exc.__class__.__name__}:{exc}')
    print(f'{some_rect=}')


if __name__ == '__main__':
    main()
