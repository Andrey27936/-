"""
Имя проекта: 1-31
Номер версии: 1.0
Имя файла: Задача 13.py
Автор: 2021 © А.И. Баскаков, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 22/05/2021
Описание: Задача 13.
#версия Python: 3.9
"""
import numpy as np 
N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
print(f'\nЗадан размер матрицы случайных целых чисел: [{N}, {M}])
np.random.seed(0)
A = np.random.randint(10, size = (N, M))
print('\nПрямоугольная матрица случайных целых чисел:\n', A)
max_z = False
i = 0
while i < len(A):
    j = 0
    while j < len(A[i]):
        if max_z is False or max_z < A[i][j]:
            max_z = A[i][j]
        j += 1
    i += 1
i = 0
while i < len(A):
    j = 0
    while j < len(A[i]):
        A[i][j] /= max_z
        A[i][j] = round(A[i][j], 1)
        j += 1
    i += 1
print("Максимальный элемент:", max_z)
print("\nМодифицированная матрица:\n", A)
