frase = input("Introduce una frase: ")

frase = frase.lower()
palabras = frase.split()
contador = 0

for palabra in palabras:
    vocales = {letra for letra in palabra if letra in "aeiou"}
    if len(vocales) >= 4:
        contador += 1

print("Número de palabras con 4 o más vocales diferentes:", contador)
