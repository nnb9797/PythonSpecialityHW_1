# 3. Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

from HW9.task1 import set_game_rules
from HW9.task2 import game_guess
from HW9.task5 import game_guess_2
from HW9.task6 import game_guess_3


if __name__ == '__main__':
    game = set_game_rules()
    game()
    game_guess(100, 10)
    game_guess_2(100, 10)
    game_guess_3(100, 10)
