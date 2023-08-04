# 3.Напишите декоратор, который сохраняет в json файл. Параметры декорируемой
# функции и результат, который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.


import json
import os.path
from typing import Callable


def logger(file_name) -> Callable:

    def inner_func(func):

        def wrapper(*args, **kwarg):
            my_dict = {func(*args, **kwarg): [arg for arg in args] + [(key, value) for key, value in kwarg.items()]}
            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, indent=4, ensure_ascii=False)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f, indent=4, ensure_ascii=False)
            return func(*args, **kwarg)
        return wrapper
    return inner_func


@logger('file.json')
def function_json(a, b, c) -> str:

    return a + b + c


if __name__ == '__main__':
    print(function_json(1, 2, 3))
    print(function_json(1, 2, c=3))
    print(function_json(a=1, b=2, c=3))
