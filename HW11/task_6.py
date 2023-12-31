# task_6. Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:
    """Документация прямоугольника """

    def __init__(self, side_a: int = 1, side_b: int | None = None):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)

    def get_area(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __lt__(self, other):                            # метод <
        return self.get_area() < other.get_area()

    def __eq__(self, other):                            # метод =
        return self.get_area() == other.get_area()

    def __le__(self, other):                            # метод <=
        return self.get_area() <= other.get_area()

    def __str__(self):
        return f"прямоугольник со сторонами: {self._side_a}  и  {self._side_b} и периметром: {self.get_perimeter()}"


if __name__ == '__main__':
    rect1 = Rectangle(4, 6)
    rect2 = Rectangle(4, 6)
    rect3 = rect1 + rect2

    print("\nРезультат сложения:")
    print(f"{rect1} + {rect2} = {rect3}")

    rect4 = Rectangle(14, 16)
    rect5 = Rectangle(4, 6)
    rect6 = rect4 - rect5

    print("\nРезультат вычитания:")
    print(f"{rect4} - {rect5} = {rect6}")
    print("\nCравнение прямоугольников:\n")
    print(f"{rect1 } < {rect2} - {rect1 < rect2}")
    print(f"{rect1} > {rect2} - {rect1 > rect2}")
    print(f"{rect1} <= {rect2} - {rect1 <= rect2}")
    print(f"{rect1} >= {rect2} - {rect1 >= rect2}")
    print(f"{rect1} == {rect2} - {rect1 == rect2}")
    print(f"{rect1} != {rect2} - {rect1 != rect2}")
    print("\nДокументация прямоугольника:\n")
    print({help(Rectangle)})
