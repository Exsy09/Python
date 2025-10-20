import random

numeros = [random.randint(1, 50) for _ in range(100)]

print("Números generados:")
print(numeros)

mayor = max(numeros)
menor = min(numeros)

mas_frecuente = max(set(numeros), key=numeros.count)
veces = numeros.count(mas_frecuente)

print("\nRESULTADOS:")
print("Número mayor:", mayor)
print("Número menor:", menor)
print("Número que más se repite:", mas_frecuente)
print("Veces que aparece:", veces)

