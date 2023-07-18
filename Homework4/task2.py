# 2. Напишите функцию:
# * принимающую на вход только ключевые параметры и возвращающую словарь,
# * где ключ — значение переданного аргумента,
# * значение — имя аргумента. Если ключ не хешируем,
# * используйте его строковое представление.


"""Hashable dictionary function"""

def hashable_dicts(**kwargs):
    reverse_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        reverse_dict[value] = key
    return reverse_dict


print(hashable_dicts(english_writers=["Charles Dickens", "John Galsworthy", "Edgar Allan Poe"], \
                     english_poets={1: "George Gordon Byron", 2: "William Shakespeare", 3: "Rudyard Kipling"}))