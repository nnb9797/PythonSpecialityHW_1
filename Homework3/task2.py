# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


initial_list = [0, 8, 8, 2, 3, "F", "T", "F", 3, "o", 46, "g", "0", 0]


def double_elements(elements_list: list) -> list:
    return list(set([i for i in elements_list if elements_list.count(i) > 1]))


def main():
    print(f"Список повторяющихся элементов:{initial_list} \nРезультирующий список повторяющихся элементов\
 без дубликатов: {double_elements(initial_list)}")


if __name__ == "__main__":
    main()