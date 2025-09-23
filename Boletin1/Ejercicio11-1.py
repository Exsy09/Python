import random

contador = 0
iguales = False

while iguales == False:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 == dado2:
        iguales = True
    print(dado1, "-", dado2)
    contador += 1
print("Veces que se ha tirado: ", contador)

