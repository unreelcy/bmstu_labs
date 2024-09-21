"""
Лабораторная работа по программированию №2
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б (4 - 1 вариант)

Программa для определения y по введенному x
"""

# Программа 2: Вариант 4
# Блок 0: Подключение необходимых библиотек
from math import sqrt, log10


# Блок 1: Ввод исходных данных
x = float(input("Введите значение коэффициенита x: "))

# Блок 2: Вычиление значения функции
if x <= -5:
    y = -x - 5
elif x <= 0:
    y = x + 5
elif x < 5:
    y = sqrt(25 - x ** 2)
else:
    y = log10(x - 4)

# Блок 2: Вывод значения функции
print("Значение функции для заданного x: {:7f}".format(y))


''' TeSt CaSeS
-10
>Значение функции для заданного x: 5.000000

-4
>Значение функции для заданного x: 1.000000

1
>Значение функции для заданного x: 4.898979

6
>Значение функции для заданного x: 0.301030

14
>Значение функции для заданного x: 1.000000
'''
