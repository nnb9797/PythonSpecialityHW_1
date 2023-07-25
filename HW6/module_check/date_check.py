# Модуль проверки даты

from datetime import datetime
from sys import argv

__all__ = ["check_year", "date_validator"]

def leap_year_check(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    YEARS = range(1, 9999)
    year = int(date.split(".")[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False


def check_year(year: str) -> bool:
    try:
        _ = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except:
        return False


def date_validator(date_for_check: str) -> str:
    if check_year(date_for_check):
        return "Год является високосным" if leap_year_check(date_for_check) else "Год не является високосным"
    else:
        return f"Некорректный ввод даты"


if __name__ == "__main__":
    if len(argv) == 2:
        _, date = argv
        print(date_validator(date))
    else:
        print("Не введена дата")
