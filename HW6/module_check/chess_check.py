# Модуль проверки расстановки фигур на шахматной доске


import random as rnd

__all__ = ["check_queens", "generate_positions"]

queens_amount: int = 8
board_size: int = 8


def check_queens(positions: list[tuple]) -> bool:

    result = True

    if len(positions) != queens_amount:
        result = False
    else:
        for i in range(queens_amount - 1):
            if not result:
                break
            row_1, col_1 = positions[i]
            for j in range(i + 1, queens_amount):
                row_2, col_2 = positions[j]

                if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                    result = False
                    break

    return result


def generate_positions() -> list[tuple[int, int]]:

    result = []
    for i in range(board_size):
        result.append((i, rnd.randint(0, board_size - 1)))
    return result
