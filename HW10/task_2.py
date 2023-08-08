# 2. Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, height: int, width=None):
        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    def get_perimetr(self):
        return 2 * (self.height + self.width)

    def get_area(self):
        return self.width * self.height


spam = Rectangle(15, 22)
eggs = Rectangle(10)

print(f'{spam.get_area() =}')
print(f'{spam.get_perimetr()= }')
print(f'{eggs.get_area()= }')
print(f'{eggs.get_perimetr()= }')
