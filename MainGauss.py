from SLAE import SLAE

slae = SLAE(3, 3, [[1, 1, 1], [1, -1, 2], [2, -1, -1]], [6, 5, -3])

vector = slae.GaussMethod()

print(vector)

