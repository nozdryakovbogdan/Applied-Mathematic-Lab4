import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import splu

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

    # Создаем разреженную матрицу в формате CSR
    A_sparse = csr_matrix(A)

    # Находим LU-разложение разреженной матрицы
    lu = splu(A_sparse)

    # Решаем систему линейных уравнений
    x = lu.solve(b)

    # Вычисляем число обусловленности и норму невязки
    cond = np.linalg.cond(A)
    residual = np.linalg.norm(np.dot(A,x)-b)
    conds.append(cond)
    residuals.append(residual)

plt.plot(ks, conds, label="cond(A)")
plt.plot(ks, residuals, label="||Ax-b||")
plt.legend()
plt.show()

input()
