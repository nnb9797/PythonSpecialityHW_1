
# 5. Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое
#  в виде одноимённых pickle файлов.


import json
import pickle
from pathlib import Path


def get_pickle(name: dict, json_data: Path) -> None:
    with open(json_data, 'wb') as f_pic:
        pickle.dump(name, f_pic)


def read_json(file: Path) -> dict[str, str, str]:
    with open(file, 'r', encoding='utf-8') as f_js:
        json_file = json.load(f_js)
    return json_file


def convert_json_to_pickle(file_in: Path, file_out: Path) -> None:
    get_pickle(read_json(file_in), file_out)


if __name__ == '__main__':
    convert_json_to_pickle(Path('task4.json'), Path('json_pickle.bin'))