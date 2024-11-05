"""
Лабораторная работа по программированию №2 Часть 2
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б

Программa для определения принадлежит ли точка "бабочке"
"""

# Программа 3:
# Блок 1: Ввод исходных данных
x = float(input("Введите значение координаты x: "))
y = float(input("Введите значение координаты y: "))

# Блок 2: Определение принадлежности точки к замкнутой области
flag = False
if x >= -9:
    if x < -8:
        if 7 * (x + 8) ** 2 + 1 <= y <= -1/8 * (x + 9) ** 2 + 8:
            flag = True
    elif x <= -2:
        if 1/3 * (x + 5) ** 2 - 7 <= y <= -1/16 * x ** 2 or 1/49 * (x + 1) ** 2 <= y <= -1/8 * (x + 9) ** 2 + 8:
            flag = True
    elif x < -1:
        if any((-2 * (x + 1) ** 2 - 2 <= y <= -1/16 * x ** 2,
                1/49 * (x + 1) ** 2 <= y <= -1/8 * (x + 9) ** 2 + 8,
                y == -3/2 * x + 2)):
            flag = True
    elif x == -1:
        if -2 <= y <= 0 or y == 3.5:
            flag = True
    elif x <= 0:
        if 4 * x ** 2 - 6 <= y <= -4 * x ** 2 + 2 or y == -3/2 * x + 2:
            flag = True
    elif x < 1:
        if 4 * x ** 2 - 6 <= y <= -4 * x ** 2 + 2 or y == 3/2 * x + 2:
            flag = True
    elif x == 1:
        if -2 <= y <= 0 or y == 3.5:
            flag = True
    elif x <= 2:
        if any((-2 * (x - 1) ** 2 - 2 <= y <= -1/16 * x ** 2,
                1/49 * (x - 1) ** 2 <= y <= -1/8 * (x - 9) ** 2 + 8,
                y == 3/2 * x + 2)):
            flag = True
    elif x <= 8:
        if 1/3 * (x - 5) ** 2 - 7 <= y <= -1/16 * x ** 2 or 1/49 * (x - 1) ** 2 <= y <= -1/8 * (x - 9) ** 2 + 8:
            flag = True
    elif x <= 9:
        if 7 * (x - 8) ** 2 + 1 <= y <= -1/8 * (x - 9) ** 2 + 8:
            flag = True

# Блок 3: Вывод вердикта
print('Точка входит в область.' if flag else "Точка за границей области.")

""" TeSt CaSeS
-8
-8
-

-8
-4
+

-8
-2
-

-8
4
+

-8
8
-

-6
2
+

-6
8
-

-6
-4
+

-1
0
+

-1
-1
+

-1
-4
-

-1
3.5
+

0
-2
+

0
-8
-
"""