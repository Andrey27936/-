"""
��� �������: 1-31
����� ������: 1.0
��� �����: ������ 20.py
�����: 2021 � �.�. ��������, ���������
�������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
���� ��������: 23/05/2021
��������: ������ 20.
#������ Python: 3.9
"""
import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("�������:\r\n{}\n".format(A))

a = b = np.fliplr(A).diagonal(1)
a_prod = a.prod()
print("�������� ������� ���� �������� ���������: \n" + str(a) + "\n�� ����� = " + str(a_prod))
b = np.fliplr(A).diagonal(-1)
b_prod = b.prod()
print("�������� ������� ���� �������� ���������: \n" + str(b) + "\n�� ����� = " + str(b_prod))
