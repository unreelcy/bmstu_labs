"""
Лабораторная работа по программированию №1
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б (10 вариант)

Программа по:
   определению V, S полн, S конуса шарового сектора (конус + шаровой сегмент)
   из R, H_конуса
"""


# Блок 1 - подключение необходимых модулей
from math import pi, sqrt

# Блок 2 - ввод исходных значений
r_sphere = float(input('Введите радиус шара: '))  # радиус шара
if r_sphere > 0:
    h_cone = float(input('Введите высоту конуса: '))  # высота конуса
    if 0 < h_cone < r_sphere:
        # Блок 3 - вычисление основных параметров
        r_cone = sqrt(h_cone * (2 * r_sphere - h_cone))  # радиус основания конуса
        l_cone_facet = sqrt(r_cone ** 2 + h_cone ** 2)  # длина образующей конуса
        s_cone_base = pi * r_cone ** 2  # площадь основания конуса

        # Блок 4 - вычисление параметров объема
        v_sphere = 4 / 3 * pi * r_sphere ** 3  # v шара
        v_small_segment = pi * h_cone ** 2 * (3 * r_sphere - h_cone) / 3  # v отсеченной части шара
        v_big_segment = v_sphere - v_small_segment  # v большей части шара после отсечения
        v_cone = s_cone_base * h_cone * 1/3  # v конуса
        v_sector = v_big_segment + v_cone  # v шарового сектора

        # Блок 5 - вычисление параметров площади
        s_sphere = 4 * pi * r_sphere ** 2  # s поверхности шара
        s_small_segment = 2 * pi * r_sphere * h_cone  # s сферической части отсеченного сегмента
        s_big_segment = s_sphere - s_small_segment  # s большей сферической части шара после отсечения
        s_cone = pi * r_cone * l_cone_facet  # s боковой поверхности конуса
        s_sector = s_big_segment + s_cone  # s шарового сектора

        # Блок 6 - вывод вычисленных значений
        print("Объем шарового сектора :", round(v_sector, ndigits=7))  # v шарового сектор
        print("Площадь шарового сектора :", round(s_sector, ndigits=7))  # s шарового сектора
        print("Площадь боковой поверхности конуса :", round(s_cone + s_cone_base, ndigits=7))  # s поверхности конуса
    else:
        print('\n--ERROR--\nЗначение высоты не может быть меньше/равно нулю или больше радиуса.')
else:
    print('\n--ERROR--\nЗначение радиуса не может быть меньше/равно нулю.')
