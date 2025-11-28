import random

n = int(input("Dame un numero: "))
numeros = [random.randint(10, 1000) for _ in range(n)]
print(numeros)

recuperar = int(input("Numero a recuperar: "))

try:
    if recuperar < 0:
        raise ValueError("No se pudo recuperar")
    print("El numero en la posición", recuperar, "es", numeros.pop(recuperar))
except:
    print("No se pudo recuperar")
