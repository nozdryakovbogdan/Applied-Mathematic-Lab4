import numpy as np
import matplotlib.pyplot as plt

# Определяем матрицу A и вектор b
n = 10
ks = range(1,11)
conds = []
residuals = []

for k in ks:
    A = np.zeros((n,n))
    b = np.zeros(n)
    for i in range(n):
        for j in range(n):
            A[i,j] = 1/(i+j+k)
        b[i] = i+1
    x = np.linalg.solve(A,b)
    cond = np.linalg.cond(A)
    residual = np.linalg.norm(np.dot(A,x)-b)
    conds.append(cond)
    residuals.append(residual)

plt.plot(ks, conds, label="cond(A)")
plt.plot(ks, residuals, label="||Ax-b||")
plt.legend()
plt.show()
input()