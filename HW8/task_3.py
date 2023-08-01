# ------------------------------------------- 3 -----------------------------
# Напишите функцию, которая сохраняет
# созданный в прошлом задании файл в формате CSV.


import json
from pathlib import Path
import csv

def convert_json_to_csv(file: Path):
    with (open(file, 'r', encoding='utf-8') as fj,
          open(f'{file.stem}.csv', 'w', encoding='utf-8', newline='') as fc):

        spam = json.load(fj)
        temp_list = []
        for level, value in spam.items():
            for id_cod, name in value.items():
                temp_list.append({'level': int(level), 'id_cod': id_cod, 'name': name})

        csv_temp = csv.DictWriter(fc, dialect='excel', fieldnames=['level', 'id_cod', 'name'])
        csv_temp.writeheader()
        csv_temp.writerows(temp_list)

if __name__ == '__main__':
    convert_json_to_csv(Path('bd_task2.json'))
