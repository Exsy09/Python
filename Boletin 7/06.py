import random
import statistics

n = int(input("Dame un numero: "))
numeros = [random.randint(10, 1000) for _ in range(n)]

print(numeros)

mayor = max(numeros)
menor = min(numeros)
media = round(statistics.mean(numeros), 2) # Media aritmetica
posMayor = [i for i, x in enumerate(numeros) if x == mayor] # muestra todas las posiciones de un elemento
posMenor = [i for i, x in enumerate(numeros) if x == menor]

Mayor = str(posMayor)
Menor = str(posMenor)

Mayor = Mayor.replace("[", "")
Mayor = Mayor.replace("]", ".")
Menor = Menor.replace("[", "")
Menor = Menor.replace("]", ".")

print("Número mayor es ", mayor, "y sus posiciones son", Mayor, "\nNúmero menor es ", menor, "y sus posiciones son", Menor, "\nMedia aritmetica es ", media)