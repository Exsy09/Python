import random

i = int(input("Numero 1: "))
j = int(input("Numero 2: "))
if i > j:
    print(random.randint(j, i))