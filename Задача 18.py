"""
��� �������: 1-31
����� ������: 1.0
��� �����: ������ 18.py
�����: 2021 � �.�. ��������, ���������
�������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
���� ��������: 23/05/2021
��������: ������ 18.
#������ Python: 3.9
"""
import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("�������:\r\n{}\n".format(A))

a = np.diagonal(A)
a_sum = a.sum()
print("������� ���������: \n" + str(a) + "\n Ÿ ����� = " + str(a_sum))
b = np.fliplr(A).diagonal(0)
b_sum = b.sum()
print("�������� ���������: \n" + str(b) + "\n Ÿ ����� = " + str(b_sum))
