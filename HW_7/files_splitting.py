from pathlib import Path
from typing import TextIO


__all__ = ['files_splitting']


def _file_reading(fd: TextIO) -> str:
    line = fd.readline()
    if line == '':
        fd.seek(0)
        return _file_reading(fd)
    return line[:-1]


def files_splitting(numbers: Path, strings: Path, result: Path) -> None:
    with (
        open(numbers, 'r', encoding='utf-8') as f_num,
        open(strings, 'r', encoding='utf8') as f_str,
        open(result, 'w', encoding='utf-8') as f_res
    ):
        len_str = sum(1 for _ in f_str)
        len_num = sum(1 for _ in f_num)
        for _ in range(max(len_str, len_num)):
            name = _file_reading(f_str)
            two_num = _file_reading(f_num)
            num_i, num_f = two_num.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_res.write(f'{name.lower()} {-mult}\n')
            elif mult > 0:
                f_res.write(f'{name.upper()} {int(-mult)}\n')
