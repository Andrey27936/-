"""
 Имя проекта: 1-31
 Номер версии: 1.0
 Имя файла: Задача 11.ру
 Автор: 2021 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 22/05/2021
 Описание: Задача 11.
 #версия Python: 3.9
"""
import random

N = 4
M = 5

L = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)


l_row = A[L - 1].copy()

i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        A[i][j] += l_row[j]
        j += 1

    i += 1

print("Моифицированная матрица:")
print_matrix(A)
