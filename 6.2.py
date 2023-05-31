python
import numpy as np

# Определяем матрицу A и вектор b
n = 10
A = np.zeros((n,n))
b = np.zeros(n)
for i in range(n):
    for j in range(n):
        A[i,j] = 1/(i+j+k)
    b[i] = i+1

# Вычисляем решение системы Ax=b
x = np.linalg.solve(A,b)

# Вычисляем число обусловленности матрицы A
cond = np.linalg.cond(A)

# Вычисляем точность решения
residual = np.linalg.norm(np.dot(A,x)-b)

# Выводим результаты
print("k = ", k)
print("cond(A) = ", cond)
print("||Ax-b|| = ", residual)
input()
