#    7. Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
#    Распечатайте его как pickle строку.

import pickle
from pathlib import Path


def reader_csv(file: Path) -> str:
    with open(file, 'r', encoding='utf-8') as f_csv:
        return f_csv.read()


def print_pickle(file_csv: str) -> None:
    print(pickle.dumps(file_csv))


def csv_to_pickle(file_csv: Path):
    print_pickle(reader_csv(file_csv))


if __name__ == '__main__':
    csv_to_pickle(Path('pickle_to_csv.csv'))
