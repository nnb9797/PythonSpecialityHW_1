#3. Возьмите задачу о банкомате из семинара 2.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from datetime import date


account = 0
count = 0
taking_from_percent = 0.015
adding_to_percent = 0.03
wealth_tax = 0.01

"""Adding money to the account function"""

def add_to_account(my_money: float) -> None:
    global account
    global count
    account += my_money
    count += 1
    if count % 3 == 0:
        account = account + adding_to_percent * account
        print("Начислены проценты в размере: ", adding_to_percent * account)


"""Taking money from the account function"""

def take_from_account(my_money: float) -> None:
    global account
    global count
    account -= my_money
    count += 1

    if my_money * taking_from_percent < 30:
        account -= 30
        print("Списана комиссия за снятие наличных: ", 30, "$")
    elif my_money * taking_from_percent > 600:
        account -= 600
        print("Списана комиссия за снятие наличных: ", 600, "$")
    else:
        account -= my_money * taking_from_percent
        print("Списана комиссия за снятие наличных: ", my_money * taking_from_percent)
    if count % 3 == 0:
        account = account + adding_to_percent * account
        print("Начислены проценты в размере: ", adding_to_percent * account)


"""Exiting programme function"""

def exit_bank():
    if action == "5":
        print("Всего доброго!\n")
        exit()


"""Checking account balance function"""

def check_account() -> int:
    while True:
        my_money = int(input("Введите сумму, кратную 50$\n"))
        if my_money % 50 == 0:
            return my_money


operation_list = []

while True:
    action = input("Введите номер операции, которую хотите совершить:  "
                   "\n1 - пополнить счет\n2 - снять наличные\n3 - баланс счета  "
                   "\n4 - вывести историю операций\n5 - выйти из приложения\n")

    if action == "2":
        if account > 5_000_000:
            account = account - account * wealth_tax
            print("Списан налог на богатство: ", account * wealth_tax)
        my_money = check_account() - account * wealth_tax
        if my_money < account:
            take_from_account(my_money)

            operation_list.append([str(date.today()), -1 * my_money, action])
        else:
            print("На счете недостаточно средств для совершения операции\n")
        if account > 5_000_000:
            account = account - account * wealth_tax
            print("Списан налог на богатство: ", account * wealth_tax)
        print("Баланс Вашего счета: ", account, "$")
    elif action == "1":
        my_money = check_account()
        add_to_account(my_money)
        if account > 5_000_000:
            account = account - account * wealth_tax
            print("Списан налог на богатство: ", account * wealth_tax)
        print("Баланс Вашего счета: ", account, "$")

        operation_list.append([str(date.today()), my_money, action])

    elif action == "3":
        print("Баланс Вашего счета: ", account, "$")
    elif action == "4":
        print(operation_list)
    elif action == "5":
        exit_bank()
    elif action != "1" or "2" or "3" or "4" or "5":
        print("Некорректный выбор операции. Попробуйте, пожалуйста, снова.")
        print(operation_list)
    else:
        exit_bank()