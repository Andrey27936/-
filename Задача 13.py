"""
��� �������: 1-31
����� ������: 1.0
��� �����: ������ 13.py
�����: 2021 � �.�. ��������, ���������
�������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
���� ��������: 22/05/2021
��������: ������ 13.
#������ Python: 3.9
"""
import numpy as np 
N = int(input("������� ���������� �����: "))
M = int(input("������� ���������� ��������: "))
print(f'\n����� ������ ������� ��������� ����� �����: [{N}, {M}])
np.random.seed(0)
A = np.random.randint(10, size = (N, M))
print('\n������������� ������� ��������� ����� �����:\n', A)
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
print("������������ �������:", max_z)
print("\n���������������� �������:\n", A)
