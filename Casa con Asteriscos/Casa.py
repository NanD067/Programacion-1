import numpy as np

n = 12
matriz = np.full((25, 35), ' ', dtype="U1")

for i in range(n+1):
    j = (17 * i) // n
    matriz[i, 17 - j] = "*"
    matriz[i, 17 + j] = "*"

for j in range(35):
    matriz[n, j] = "*"

for i in range(n, 25):
    matriz[i, 2] = "*"
    matriz[i, 32] = "*"

for j in range(2, 33):
    matriz[24, j] = "*"

for i in range(15, 22):
    for j in range(5, 12):
        if i -- 15 or i == 21 or j == 5 or j == 11 or i == 18 or j == 8:
            matriz[i, j] = "*"

for i in range(15, 22):
    for j in range(23, 30):
        if i -- 15 or i == 21 or j == 23 or j == 29 or i == 18 or j == 26:
            matriz[i, j] = "*"

for i in range(18, 25):
    for j in range(15, 20):
        if i == 18 or j == 15 or j == 19 or i == 24:
            matriz[i, j] = "*"

for fila in matriz:
    print(" ".join(fila))
