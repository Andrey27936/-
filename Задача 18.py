"""
Имя проекта: 1-31
Номер версии: 1.0
Имя файла: Задача 18.py
Автор: 2021 © А.И. Баскаков, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 23/05/2021
Описание: Задача 18.
#версия Python: 3.9
"""
import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

a = np.diagonal(A)
a_sum = a.sum()
print("Главная диагональ: \n" + str(a) + "\n Её сумма = " + str(a_sum))
b = np.fliplr(A).diagonal(0)
b_sum = b.sum()
print("Побочная диагональ: \n" + str(b) + "\n Её сумма = " + str(b_sum))
