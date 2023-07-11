# Напишите программу банкомат.

#   Начальная сумма равна нулю
#   Допустимые действия: пополнить, снять, выйти
#   Сумма пополнения и снятия кратны 50 у.е.
#   Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#   После каждой третей операции пополнения или снятия начисляются проценты - 3%
#   Нельзя снять больше, чем на счёте
#   При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
#   Любое действие выводит сумму денег

def calculate_tax(balance):
    if balance >= 5000000:
        # Вычитаем налог на богатство 10%
        tax = balance * 0.1
        balance -= tax
    return balance

def calculate_interest(balance, operations_count):
    if operations_count % 3 == 0 and operations_count != 0:
        # Начисляем проценты 3%
        interest = balance * 0.03
        balance += interest
        print("Начислены проценты:", interest)
    return balance

def deposit(balance):
    amount = int(input("Введите сумму для пополнения (кратную 50): "))
    if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
        return balance

    balance += amount
    return balance

def withdraw(balance):
    amount = int(input("Введите сумму для снятия (кратную 50): "))
    if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
        return balance

    if amount > balance:
        print("Недостаточно средств на счете")
        return balance

    if amount > 600:
        amount = 600
    elif amount < 30:
        amount = 30

    fee = amount * 0.015
    balance -= amount + fee
    return balance

def print_balance(balance):
    print("Остаток на счете:", balance)

def atm():
    balance = 0
    operations_count = 0

    while True:
        balance = calculate_tax(balance)

        print("Текущий баланс:", balance)

        choice = input("Выберите действие:\n"
                       "1. Пополнить\n"
                       "2. Снять\n"
                       "3. Выйти\n"
                       "Введите номер действия: ")

        if choice == "1":
            balance = deposit(balance)
            operations_count += 1
        elif choice == "2":
            balance = withdraw(balance)
            operations_count += 1
        elif choice == "3":
            print("Операция завершена")
            break
        else:
            print("Некорректный выбор")

        balance = calculate_interest(balance, operations_count)
        print_balance(balance)

atm()