"""
��� �������: 1-31
����� ������: 1.0
��� �����: ������ 17.py
�����: 2021 � �.�. ��������, ���������
�������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
���� ��������: 23/05/2021
��������: ������ 17.
#������ Python: 3.9
"""
import numpy as np

N = 4
M = 5
L = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("�������:\r\n{}\n".format(A))

a = np.random.randint(0, 10, M)
print("�������������� ������: " + str(a))
print("\n L = " + str(L))

row = np.random.randint(low=-9, high=10, size=M)
print("������ ��� �������: {}".format(row))
A = np.insert(A, L, row, axis=0)

print("����� �������:\r\n{}\n".format(A))
