# Модуль проверки расстановки фигур на шахматной доске


import random as rnd

__all__ = ['check_queens', 'gen_positions']

queens_amount: int = 8  # максимальное кол-во ферзей
board_size: int = 8  # размер доски


def check_queens(positions: list[tuple]) -> bool:

    result = True

    if len(positions) != queens_amount:
        result = False
    else:
        for i in range(queens_amount - 1):  # берем ферзей по списку, исключая последнего (сам себя бить не может)
            if not result:
                break
            row_1, col_1 = positions[i]
            for j in range(i + 1, queens_amount):  # проверяем со следующими до конца списка
                row_2, col_2 = positions[j]
                # Ферзи на одной линии, если координаты строки или столбца у них равны.
                # Ферзи на одной диагонали, если позицию второго можно получить из позиции первого смещением на равное
                # количество строк и столбцов в любую из сторон
                if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                    result = False
                    break

    return result


def gen_positions() -> list[tuple[int, int]]:

    result = []
    for i in range(board_size):
        result.append((i, rnd.randint(0, board_size - 1)))
    return result
