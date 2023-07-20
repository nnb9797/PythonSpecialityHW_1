# 6. Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# Для вывода результата используйте «принт»
# без перехода на новую строку.

min_number = 2
max_number = 10
column = 4

[[print(f'{k:>} * {j:>2} = {k * j:>2}\n\n', end='') if (j == max_number and k == i + column - 1)
else print(f'{k:>} * {j:>2} = {k * j:>2}\n', end='') if k == i + column - 1
else print(f'{k:>} * {j:>2} = {k * j:>2}\t\t', end='') for k in range(i, i + column)]
 for i in range(min_number, max_number, column) for j in range(min_number, max_number + 1)]
