"""
Лабораторная работа по программированию №2
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б (4 - 1 вариант)

2 Программы:
    1. Решение квадратного уравнения
    2. Определение находится ли точка в "бабочке"
"""
# Программа 1:
# Блок 0: Подключение необходимых библиотек
from math import sqrt


# Блок 1: Ввод исходных данных
a = float(input('Введите значение коэффициента a: '))
b = float(input('Введите значение коэффициента b: '))
c = float(input('Введите значение коэффициента c: '))

# Блок 2: Вычисление корней или определение их отсутствия
if a == 0:
    if b == 0:
        if c == 0:
            print("x ∍ R")
        else:
            print("x ∍ ∅")
    else:
        x = (-c) / b
        print("Корень: {:7f}".format(x))
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Уравнение не имеет корней.")
    else:
        if d == 0:
            x0 = (-b) / (2 * a)
            print("Корень: {:7f}".format(x0))
        else:
            sqrt_d = sqrt(d)
            x1 = (-b - sqrt_d) / (2 * a)
            x2 = (-b + sqrt_d) / (2 * a)
            print("Первый корень: {:7f}".format(x1))
            print("Второй корень: {:7f}".format(x2))

''' TeSt CaSeS
1
-3
2
>Первый корень: 2.000000
>Второй корень: 1.000000

1
1
1
>Уравнение не имеет корней.

1
2
1
>Корень: -1.000000

0
0
0
>x ∍ R

0
1
1
>Корень: -1.000000

0
0
1
>x ∍ ∅
'''

# Программа 2:
# <