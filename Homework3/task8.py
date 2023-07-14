# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# * Какие вещи взяли все три друга

# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует

# * Для решения используйте операции с множествами.
# * *Код должен расширяться
# на любое большее количество друзей.

friends = {"Sam": ("water", "sugar", "meat", "bread", "tea", "salt", "oil"),\
                        "Tom": ("sugar", "matches", "milk", "bread", "salt", "cheese", "sausages"),\
                        "Bob": ("coffee", "fish", "rice", "bacon", "salt", "bread", "honey")}

all_things = tuple()
for pack in [items for items in friends.values()]:
    all_things += pack
all_things = set(all_things)


def things_all_have(equipment: dict[str, tuple]) -> str:
    popular = all_things.copy()
    for value in equipment.values():
        popular.intersection_update(value)
    return "Все друзья взяли с собой в поход:\n" + ", ".join(list(popular))


def unique_thing(equipment: dict[str, tuple]) -> str:
    unique_set = []
    for friend, value in equipment.items():
        my_equipment = set(value)
        for current_friend, current_value in equipment.items():
            if friend != current_friend:
                my_equipment.difference_update(current_value)
        unique_set.append((friend, my_equipment if my_equipment else {"Уникальных вещей нет"}))

    return "Список уникальных вещей:\n" + "\n".join([f"{items[0]}: "f'{", ".join([item for item in list(items[1])])}'
                                                     for items in unique_set])


def thing_all_have_except_one(equipment: dict[str, tuple]) -> str:
    result = {}
    for name, items in equipment.items():
        current_equipment = all_things.copy()
        for current_name, current_items in equipment.items():
            if name != current_name:
                current_equipment.intersection_update(set(current_items))
        result[name] = current_equipment.difference(items)
    return "Это взяли с собой все друзья, кроме:\n" + \
        '\n'.join(f'{name}: {", ".join([item for item in items])}' for name, items in result.items())


print(things_all_have(friends))
print()
print(unique_thing(friends))
print()
print(thing_all_have_except_one(friends))
print()