# 2.Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.


import json
import time
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        dump_dict = {}
        while self.memory:
            dump_dict.update(self.memory.popleft())
        with open(f'{int(time.time())}.json', 'w', encoding='utf-8') as f:
            json.dump(dump_dict, f, indent=2)


k_value = 2
with Factorial(k_value) as factorial_calculator:
    factorial_calculator(5)
    factorial_calculator(7)
    factorial_calculator(9)
    print("Memory:", factorial_calculator.old())
