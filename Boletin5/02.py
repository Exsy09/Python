numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))

if numero1 < numero2:
    for i in range(1, numero1 + 1):
        if numero1 % i == numero2 % i == 0:
            print(i)

if numero2 < numero1:
    for i in range(1, numero2 + 1):
        if numero1 % i == numero2 % i == 0:
            print(i)