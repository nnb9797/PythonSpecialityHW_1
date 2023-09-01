# ------------------------------------------- 2 -----------------------------
"""
📌 Создайте функцию аналог get для словаря.
📌 Помимо самого словаря функция принимает ключ и значение по умолчанию.
📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
📌 Реализуйте работу через обработку исключений.
"""


def get_value_from_dict(dictionary, key, def_value=None):
    try:
        value = dictionary[key]
    except KeyError:
        value = def_value
    return value


my_dict = {"a": 1, "b": 2, "c": 3}

key_to_check = "b"
default_value = -1

result = get_value_from_dict(my_dict, key_to_check, default_value)
print(f"Значение для ключа '{key_to_check}': {result}")

key_to_check = "d"
result = get_value_from_dict(my_dict, key_to_check, default_value)
print(f"Значение для ключа '{key_to_check}': {result}")
