"""
 Имя проекта: 1-31
 Номер версии: 1.0
 Имя файла: Задача 6.ру
 Автор: 2021 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 22/05/2021
 Описание: Задача 6.
 #версия Python: 3.9
"""
import random

N = 4
M = 6


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


def get_average(row):
    sum = 0
    for element in row:
        sum += element

    return sum/len(row)


def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1

    return column


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

sum = 0

i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        sum += A[i][j]
        j += 1

    i += 1

i = 0
new_row = []
while i < len(A):
    j = 0

    while j < len(A[i]):
        if len(new_row) <= j:
            new_row.append(A[i][j])
        else:
            new_row[j] += A[i][j]
        j += 1

    i += 1

i = 0
while i < len(new_row):
    new_row[i] = new_row[i]/sum
    i += 1

A.append(new_row)

print("Сумма всех элементов:", sum)
print("Модифицированная матрица:")
print_matrix(A)
