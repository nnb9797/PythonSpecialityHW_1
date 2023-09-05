# task_6. Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов

import json
import os
from functools import wraps
from random import randint
from typing import Callable


def game_counter(number):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(number):
                print(f'Задание_6.\nЯ предлагаю Вам отгадать загаданное мной число. \nИгра № {i+1}')
                results.append(func(*args, **kwargs))

            return tuple(results)
        return wrapper
    return dec


def attempts_checker(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(guess: int, attempts: int):
        guess = guess if 1 < guess < 100 else randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else randint(1, 10)
        return func(guess, attempts)
    return wrapper


def logger(file_name) -> Callable:

    def inner(func):
        @wraps(func)
        def wrapper(number, tries):
            my_dict = {str(func(number, tries)): (number, tries)}
            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, indent=4, ensure_ascii=False)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f, indent=4, ensure_ascii=False)
            return func(number, tries)
        return wrapper
    return inner

@game_counter(3)
@attempts_checker
@logger('game_guess.json')
def game_guess_3(num_sc, attempts):

    result_attempts = 1
    while attempts:
        print(f'У Вас следующее количество попыток: {attempts}.', end=' ')
        attempts -= 1
        num = int(input('Введите число в диапазоне от 1 до 100: '))
        if num == num_sc:
            print(f'Поздравляю! Вы угадали. Загаданное число: {num}')
            return result_attempts
        else:
            advice = ['больше', 'меньше']
            print(f'Загаданное число {advice[num > num_sc]}')
            result_attempts += 1
    else:
        print(f'К сожалению, Вы проиграли. Загаданное число: {num_sc}')

    return result_attempts


if __name__ == '__main__':
    # help(game_guess)
    game_guess_3(100, 10)
