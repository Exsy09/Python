import random
import statistics

n = int(input("Dame un numero: "))
numeros = [random.randint(10, 1000) for _ in range(n)]

print(numeros)

mayor = max(numeros)
menor = min(numeros)
media = round(statistics.mean(numeros), 2) # Media aritmetica

print("Número mayor es ", mayor, "\nNúmero menor es ", menor, "\nMedia aritmetica es ", media)