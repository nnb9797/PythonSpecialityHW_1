# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


MIN = 2
MAX_1 = 9
MAX_2 = 10
for i in range(MIN, MAX_1 + 1):
    for j in range(MIN, MAX_2 + 1):
        print(f'{i} x {j} = {i * j}')
    print(' ')