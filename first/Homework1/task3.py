# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS_LIMIT = 10
CURRENT_ATTEMPT = 0


num = randint(LOWER_LIMIT, UPPER_LIMIT)

while CURRENT_ATTEMPT < ATTEMPTS_LIMIT:
    user_num = int(input("Введите целое число от 0 до 1000: "))

    if user_num not in range(LOWER_LIMIT, UPPER_LIMIT):
        print("Вы ввели неверное число")
        continue
    if user_num == num:
        print("Поздравляю, Вы угадали!")
        break
    elif user_num < num:
        print("Ваше число меньше загаданного")
    else:
        print("Ваше число больше загаданного")

else:
    print("К сожалению, Ваши попытки закончились. Загаданное число: ", num)

