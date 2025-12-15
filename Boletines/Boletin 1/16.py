import random

loteria = random.randint(1, 49)
cont = 0
while cont < 6:
    print(loteria)
    loteria = random.randint(1, 49)
    cont += 1
