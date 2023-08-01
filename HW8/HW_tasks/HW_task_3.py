# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов

from pathlib import Path

from HW8.task_1 import text_json
from HW8.task_2 import fill_base
from HW8.task_3 import convert_json_to_csv
from HW8.task_4 import convert_csv_to_json
from HW8.task_5 import convert_json_to_pickle
from HW8.task_6 import convert_pickle_to_csv
from HW_task_2 import dir_inform


if __name__ == '__main__':
    # text_json(Path('task_1.txt'))
    # fill_base(Path('bd_task2.json'))
    # convert_json_to_csv(Path('bd_task2.json'))
    # convert_csv_to_json(Path('bd_task2.csv'), Path('task4.json'))
    # convert_json_to_pickle(Path('task4.json'), Path('json_pickle.bin'))
    # convert_pickle_to_csv(Path('json_pickle.bin'), Path('pickle_to_csv.csv'))
    dir_inform(Path(r'C:\Users\Natalya\PycharmProjects\pythonProject2\HW8'), 'result')
