# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# Верните все возможные варианты комплектации рюкзака.

import random

eq_list = {"tent": 4, "sleeping bag": 2, "water": 3, "food": 4, "clothes": 2, "flashlight": 1, "axe": 2,\
           "cooking pot": 2, "kettle": 1, "camera": 2, "fishing rod": 1}

max_weight = int(input("Какова грузоподъемность Вашего рюкзака? "))
counter = 0
equipment_list = []
while counter < max_weight:
    key, value = random.choice(list(eq_list.items()))
    if key in equipment_list:
        continue
    if counter + value > max_weight:
        break
    counter += value
    equipment_list += (str(key), str(value))

print(f"В рюкзак грузоподъемностью:", max_weight, "кг \nвойдут следующие пункты из списка: \n", equipment_list,\
      "\nИтого общий вес вещей составит:", counter, "кг")