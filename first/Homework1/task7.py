# Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


start_num = 1
finish_num = 999
result = None
while True:
    number = input(f"Введите число от {start_num} до {finish_num}: ")
    if start_num <= int(number) <= finish_num:
        match len(number):
            case 1:
                result = int(number) ** 2
            case 2:
                result = int(number) % 10 * int(number) // 10
            case 3:
                result = number[::-1]
        break
print(result)