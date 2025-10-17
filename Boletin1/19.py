div = int(input("Número a dividir: "))

for i in range(1, div + 1):
    if div % i == 0:
        print(i)