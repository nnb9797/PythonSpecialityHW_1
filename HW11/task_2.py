# 2.Cоздайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков - архивов
# list-архивы также являются свойствами экземпляра

class Arhiv:
    """Документация архива данных """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_arhiv = []

        cls._instance.list_arhiv.append([args])

        return cls._instance

    def __init__(self, text: str, number: int):
        self.text = text
        self.number = number


spam = Arhiv("ночной страж", 65)
print(f'{spam.text =}, {spam.number =}')

spam3 = Arhiv("дневной дозор", 1555)
print(f'{spam.text =}, {spam.number =}')

print(f'{spam.list_arhiv = }')
print({help(Arhiv)})
