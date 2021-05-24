"""
Имя проекта: 1-31
Номер версии: 1.0
Имя файла: Задача 16.py
Автор: 2021 © А.И. Баскаков, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 23/05/2021
Описание: Задача 16.
#версия Python: 3.9
"""
import numpy as np

N = 4
M = 5
L = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

print("L = " + str(L))
A = np.delete(A, (L-1), axis=0)

print("Новая матрица:\r\n{}\n".format(A))
