import random

filas = 5
columnas = 5
minas = 5

tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

minas_colocadas = 0

while minas_colocadas < minas:
    fila_aleatoria = random.randint(0, filas - 1)
    columna_aleatoria = random.randint(0, columnas - 1)
    if tablero[fila_aleatoria][columna_aleatoria] == 0:
        tablero[fila_aleatoria][columna_aleatoria] = 1
        minas_colocadas += 1

for fila in tablero:
    print(" ".join(str(celda) for celda in fila))