import random

i = int(input("Nº Tiradas: "))
j = int(input("Nº de Caras: "))

while i != 0:
    if i == 1:
        print(random.randint(i, j))
    else:
        print(random.randint(i, j), end="-")
    i = i - 1
