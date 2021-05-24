"""
��� �������: 1-31
����� ������: 1.0
��� �����: ������ 15.py
�����: 2021 � �.�. ��������, ���������
�������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
���� ��������: 23/05/2021
��������: ������ 15.
#������ Python: 3.9
"""
import numpy as np

N = 4
M = 5
H = np.random.randint(1, 4)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("�������:\r\n{}\n".format(A))

a = []
b = []
for i in range(M):
    if H in A[:, i]:
        a.append(i+1)
    else:
        b.append(i+1)
print("�������, ������� ����� ���� �� ���� ����� H - {}\n".format(a))
print("�������, ������� �� ����� ��� ����� - {}\n".format(b))

