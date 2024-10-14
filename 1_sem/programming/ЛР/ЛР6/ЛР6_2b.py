"""
Лабораторная работа по программированию №6
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 2b:
Удалить элемент с заданным индексом алгоритмически.
"""


def main():
    # Блок 0: Ввод массива и дополнительных значений
    arr = []
    print('Вводите целочисленные значения элементов по одному, ввод оканчивается пустой строкой:')
    while n := input("> "):
        while not n.replace('-', '').isalnum():
            n = input("Введите адекватное целочисленное значение\n> ")
        arr.append(int(n))

    ind = int(input('Введите индекс элемента, который надо удалить\n> '))

    # Блок 1: Удаление элемента и вывод нового массива
    for i in range(ind, len(arr) - 1):
        arr[i] = arr[i + 1]

    arr.pop(-1)

    print(arr)


if __name__ == '__main__':
    main()
