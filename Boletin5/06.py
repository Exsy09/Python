numero = input("Introduce un número: ")

conteo = [0] * 100

for cifra in numero:
    if cifra.isdigit():
        conteo[int(cifra)] += 1

print("\nFrecuencia de cada cifra: ")
for i in range (100):
    if conteo[i] > 0:
        print(f"La cifra {i} aparece {conteo[i]} veces")