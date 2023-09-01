# ------------------------------------------- 1 -----------------------------
"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
"""

CMD_GET = "get"
CMD_PUT = "put"
RICHNESS_AMOUNT = 5000000


class NotEnoughMoneyError(Exception):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "Operation denied. Not enough money on your account"


class NotMultiple50Error(Exception):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "Operation denied. The sum is not a multiple of 50"


class ATM:
    counter = 0

    def __init__(self):
        self.money = 0
        self.operations = []

    def bonus(self):
        if ATM.counter == 3:
            self.money *= 1.03
            print("3% accrued on account balance")
            ATM.counter = 0

    def rich_tax(self):
        if self.money > RICHNESS_AMOUNT:
            self.money *= 0.9
            print("10% wealth tax withheld")
            self.print()

    def put(self, cash: float) -> bool:
        if cash % 50 != 0:
            raise NotMultiple50Error()
        self.money += cash
        ATM.counter += 1
        self.bonus()
        self.print()
        self.log_operations("credited", {cash})
        return True

    def get(self, cash: float):
        if cash % 50 != 0:
            raise NotMultiple50Error()
        withdrawal_interest = cash * 0.015
        if withdrawal_interest < 30:
            withdrawal_interest = 30
        if withdrawal_interest > 600:
            withdrawal_interest = 600
        cash += withdrawal_interest
        if self.money < cash:
            raise NotEnoughMoneyError()

        self.money -= cash
        ATM.counter += 1
        self.bonus()
        self.print()
        self.log_operations("Withdrawn (including commission)", cash)

    def log_operations(self, name: str, cash: float) -> None:
        self.operations.append((name, money))

    def print(self) -> None:
        print(f"You have: {self.money:.2f} on your account")

    def print_operations(self) -> None:
        print("Operation list:") if len(self.operations) else print(
            "No operations done")
        for operation in self.operations:
            print(f"{operation[0]} = {operation[1]:.2f}")


if __name__ == "__main__":
    print("Welcome to the Bank!")
    atm = ATM()
    cmd = ""
    while cmd != "exit":
        cmd = input("Enter operation, please: (put, get, exit): ")
        atm.rich_tax()
        if cmd == CMD_PUT:
            try:
                money = float(input("Enter the sum, please"))
                atm.put(money)
            except ValueError:
                print("Enter a numerical value, please")
            except NotMultiple50Error as e:
                print(e)
        if cmd == CMD_GET:
            try:
                money = float(input("Enter the sum, please"))
                atm.get(money)
            except ValueError:
                print("Enter a numerical value, please")
            except (NotMultiple50Error, NotEnoughMoneyError) as e:
                print(e)
    atm.print_operations()
