"""
��� �������: 1-31
����� ������: 1.0
��� �����: ������ 14.py
�����: 2021 � �.�. ��������, ���������
�������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
���� ��������: 23/05/2021
��������: ������ 14.
#������ Python: 3.9
"""
import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("�������:\r\n{}\n".format(A))

Max = A.max()
print(Max)
A = A / Max

print("����� �������:\r\n{}\n".format(A))


