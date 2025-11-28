import random

azar = random.randint(1, 50)
n = int(input("Introduce numero: "))
cont = 0

while 1 <= n <= 50:
    if n == azar:
        print("BIEN, HAS GANADO")
        print("Has fallado", cont, "veces")
        break
    else:
        cont += 1
        print("Vuelve a intentarlo")
        n = int(input("Introduce numero: "))