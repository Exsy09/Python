import random
from itertools import pairwise

numeros = [random.randint(1, 1000) for _ in range(10)]

print("10 números entre el 1 y el 1000")
print(numeros)

mayor = max(numeros)
menor = min(numeros)
par = 0

for i in numeros:
    if numeros % i == 0:
        par += 1

print("El número mayor ha sido el ", mayor, "y el menor el ", menor)

print("He generado ", par, "numeros pares") # y ", impar, "numeros impares")


