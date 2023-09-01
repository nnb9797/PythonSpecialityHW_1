# ------------------------------------------- 1 -----------------------------
"""
📌 Создайте функцию, которая запрашивает числовые данные от
   пользователя до тех пор, пока он не введёт целое или вещественное число.
📌 Обрабатывайте не числовые данные как исключения.
"""


def get_numeric_input():
    while True:
        try:
            user_input = input("Введите числовое значение: ")
            numeric_value = float(user_input)
            return numeric_value
        except ValueError:
            print("Ошибка! Введите целое или вещественное число.")


numeric_input = get_numeric_input()
print("Вы ввели:", numeric_input)
