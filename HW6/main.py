# 1. Решить 7 и 8 задачи.
# 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# 4. Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


import module_check.date_check as dch
import module_check.chess_check as chess


successful_positions = 4  #  кол-во успешных расстановок ферзей

if __name__ == "__main__":
    data = input("Введите дату в формате DD.MM.YYYY: ")
    queens_positions = [
      [(0, 5), (1, 2), (4, 3), (2, 2), (7, 6), (5, 1), (2, 7), (3, 4)],
      [(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)],
    ]

    print(dch.date_validator(data))

    # проверка позиций ферзей
    for list_position in queens_positions:
        print(list_position)
        if chess.check_queens(list_position):
            print("Ферзи не бьют друг друга")
        else:
            print("Есть ферзи под ударом")

    # генерация позиций ферзей
    total_positions_generated = 0  # общее кол-во расстановок
    successful_cases = 0  # кол-во удачных расстановок
    successful_positions_list = []  # список удачных расстановок

    while successful_cases < successful_positions:
        generated_position = chess.generate_positions()
        total_positions_generated += 1
        if chess.check_queens(generated_position):
            successful_cases += 1
            successful_positions_list.append(generated_position)

    print(f"Всего сгенерировано позиций ферзей: {total_positions_generated},\n4 удачных расстановки ферзей:")
    for positions in successful_positions_list:
        print(positions)

