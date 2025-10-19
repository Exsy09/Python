import random

azar = random.randint(1, 50)
n = int(input("Introduce numero: "))
cont = 0

while 1 <= n <= 50:
    if n == azar:
        print("BIEN, HAS GANADO")
        break
    else:
        cont += 1
        if cont == 5:
            print("Has perdido, el numero era: ", azar)
            a = str(input("Quires volver a jugar: "))
            if a == "Yes":

        print("Vuelve a intentarlo")
        n = int(input("Introduce numero: "))