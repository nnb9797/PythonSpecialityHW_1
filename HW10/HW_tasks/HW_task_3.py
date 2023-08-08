# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.

class Triangle:

    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    def __str__(self):
        return f'Проверка треугольника со сторонами: {self.a}, {self.b}, {self.c}'

    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'

    @staticmethod
    def triangle_check(side_a, side_b, side_c):
        if side_a <= side_b + side_c and side_b <= side_a + side_c and side_c <= side_a + side_b:
            print('Треугольник с заданными сторонами существует')
            if side_a == side_b == side_c:
                return print('Треугольник равносторонний')
            elif side_a == side_b or side_b == side_c or side_c == side_a:
                return print('Треугольник равнобедренный')
            else:
                return print('Треугольник разносторонний')
        else:
            return print('Треугольника с такими сторонами не существует')


a = int(input('Введите длину стороны a: '))
b = int(input('Введите длину стороны b: '))
c = int(input('Введите длину стороны c: '))

triangle = Triangle(a, b, c)
print(f'{triangle}')
print(triangle.triangle_check(a, b, c))
