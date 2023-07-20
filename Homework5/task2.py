# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


my_file = "C:\\Users\\Natalya\\PycharmProjects\\pythonProject2\\Homework5\\task6"


def split_path(path: str) -> tuple[str, str, str]:
    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext


def main():
    print(split_path(my_file))


if __name__ == "__main__":
    main()