# Напишите программу, которая принимает две строки вида “a/b”
# - дробь с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

str1 = str(input('Введите дробь вида a/b : '))
str2 = str(input('Введите еще одну дробь a/b: '))
fr1 = str1.split('/')
fr2 = str2.split('/')
add = str(int(fr1[0]) * int(fr2[1]) + int(fr1[1]) * int(fr2[0])) + '/' + str(int(fr2[1]) * int(fr1[1]))
mult = str(int(fr1[0]) * int(fr2[0])) + '/' + str(int(fr1[1]) * int(fr2[1]))
print(f'Сумма введенных дробей: \n {add}, \n Произведение введенных дробей: \n {mult}')
f1 = Fraction(int(fr1[0]), int(fr1[1]))
f2 = Fraction(int(fr2[0]), int(fr2[1]))
print(f'Проверка с помощью модуля fractions \n Cумма введенных дробей: \n {f1+f2}, \n Произведение введенных дробей: \n {f1*f2}')