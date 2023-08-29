# 3.Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.


import math


class FactorialGen:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 1, start
        if step is None:
            step = 1

        self.start = start
        self.stop = stop
        self.step = step

    def calculate_factorial(self, n):
        return math.factorial(n)

    def generate(self):
        current = self.start
        while current <= self.stop:
            yield self.calculate_factorial(current)
            current += self.step


fact = FactorialGen(4, 15, 2)
for i in fact.generate():
    print(i)
