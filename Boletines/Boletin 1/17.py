import random

quiniela = random.randint(1, 3)
cont = 0
while cont < 15:
    if quiniela == 1:
        print(1)
    elif quiniela == 2:
        print(2)
    else:
        print("X")
    quiniela = random.randint(1, 3)
    cont += 1