# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


employes = ["John", "Tomas", "Samuel", "Oliver"]
salaries = [100000, 120000, 150000, 200000]
persents = ["10.25%", "10.25%", "10.25%", "10.25%"]


def gen_dict(employes: list[str], salaries: list[int], percents: list[str]):

    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(employes, salaries, map(lambda x: float(x[:-1]), percents))))}


def main():

    print(*gen_dict(employes, salaries, persents))


if __name__ == "__main__":
    main()