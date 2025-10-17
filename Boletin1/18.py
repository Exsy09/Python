import random

lucifer = random.randint(1, 1000)
cont = 0

while lucifer != 666:
    print(lucifer)
    lucifer = random.randint(1, 1000)
    cont += 1
print("El dia del juicio final será en " + str(cont) + " dias")