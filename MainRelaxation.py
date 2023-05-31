from SLAE import SLAE

slae = SLAE(3, 3, [[5, 2, -1], [-4, 7, 3], [2, -2, 4]], [12, 24, 9])

vector = slae.relaxationMethod(0.01, 0.5)

print(vector)

print()


slae = SLAE(3, 3, [[5, 2, -1], [-4, 7, 3], [2, -2, 4]], [12, 24, 9])

vector = slae.relaxationMethod(0.01, 0.25)

print(vector)