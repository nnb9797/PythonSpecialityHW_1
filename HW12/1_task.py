# 1.Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
# https://www.codecamp.ru/blog/python-deque-module/


from collections import deque


class Factorial:
    def __init__(self, k: int):
        self.memory = deque(maxlen=k)

    def __call__(self, n, *args, **kwargs):
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.memory.append({n: result})
        return self.memory[-1]

    def old(self):
        return self.memory


one = Factorial(2)
one(4)
one(14)
one(2)
one(5)
print(one.old())
