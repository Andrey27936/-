"""
��� �������: 1-31
����� ������: 1.0
��� �����: ������ 19.py
�����: 2021 � �.�. ��������, ���������
�������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
���� ��������: 23/05/2021
��������: ������ 19.
#������ Python: 3.9
"""
import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("�������:\r\n{}\n".format(A))

a = np.diagonal(A, 1)
a_sum = a.sum()
print("�������� ������� ���� ������� ���������: \n" + str(a) + "\n�� ����� = " + str(a_sum))
b = np.diagonal(A, -1)
b_sum = b.sum()
print("�������� ������� ���� ������� ���������: \n" + str(b) + "\n�� ����� = " + str(a_sum))
