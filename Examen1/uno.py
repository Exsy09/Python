import random

numero = int(input("Introduce número maximo: "))
azar = random.randint(1, numero)
cont = 0
print("5 números pares y diferentes comprendidos entre el 1 y el", numero, ": ")
while cont < 5:
    if azar % 2 == 0:
        print(azar)
        azar = random.randint(1, numero)
        cont += 1
    elif numero < 10:
        print("Numero no valido")
        break
    else:
        azar = random.randint(1, numero)