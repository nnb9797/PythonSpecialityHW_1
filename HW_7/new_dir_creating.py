from pathlib import Path
import os


def new_dir_creating(name_dir: str):
    name = Path(Path.cwd() / name_dir)
    if not name.exists():       # проверка наличия дир-ии
        name.mkdir()            # создание директории
    os.chdir(name)              # переход в созданный каталог, делая его текущим


