"""
��� �������: 1-31
����� ������: 1.0
��� �����: ������ 16.py
�����: 2021 � �.�. ��������, ���������
�������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
���� ��������: 23/05/2021
��������: ������ 16.
#������ Python: 3.9
"""
import numpy as np

N = 4
M = 5
L = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("�������:\r\n{}\n".format(A))

print("L = " + str(L))
A = np.delete(A, (L-1), axis=0)

print("����� �������:\r\n{}\n".format(A))
