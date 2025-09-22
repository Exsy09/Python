import random

#cont = 0
#a = 1
#b = 6

#while a != b:
#    a = random.randint(1, 6)
#    b = random.randint(1, 6)
#    print(a, " - ", b)
#    cont += 1
#print("Nº Tiradas: ", cont)

# Otra manera

a = 1
b = 1
igual = False
cont = 0
while igual == False: # 'not igual' funciona igual y está más optimizado
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    if a == b:
        igual = True
    cont += 1
    print(a, " - ", b)
print("Nº Tiradas: ", cont)