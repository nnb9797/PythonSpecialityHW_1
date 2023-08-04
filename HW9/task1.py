# 1.  Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
#  Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable
from random import randint


def set_game_rules() -> Callable:
    num_range = int(input('Задание_1.\nЗадайте, пожалуйста, диапазон угадываемых чисел от 1 до 100: '))
    attempts = int(input('Задайте, пожалуйста, число попыток от 1 до 10: '))
    num_sc = randint(1, num_range)

    def inner() -> None:
        nonlocal num_range, attempts
        while attempts:
            print(f'{attempts}-я попытка.', end=' ')
            attempts -= 1
            num = int(input('Введите, пожалуйста, число в заданном Вами диапазоне: '))
            if num == num_sc:
                print(f'Поздравляю, Вы угадали! Загаданное число: {num}')
                break
            else:
                advice = ['больше', 'меньше']
                print(f'Загаданное число {advice[num > num_sc]}')
        else:
            print(f'К сожалению, Вы проиграли. Загаданное число: {num_sc}')
    return inner


def main():
    game = set_game_rules()
    game()


if __name__ == '__main__':
    main()
