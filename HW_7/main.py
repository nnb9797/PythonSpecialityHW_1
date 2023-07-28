# 2.Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from pathlib import Path
from fill_numbers import fill_numbers
from name_generator import name_generator
from files_splitting import files_splitting
from create_files import create_files
from create_files_2 import create_files_2
from group_renaming import group_renaming
from new_dir_creating import new_dir_creating

if __name__ == '__main__':
    fill_numbers(20, 'numbers.txt')
    name_generator(10, 4, 7, Path('names.txt'))
    files_splitting(Path('numbers.txt'), Path('names.txt'), Path('result.txt'))
    create_files('bin', count=10)

    data = {
        'txt': 4,
        'zip': 3,
    }

    create_files_2(data)
    group_renaming(4, 'bin', 'zip', [2, 4], "new")
    new_dir_creating("new_dir")
