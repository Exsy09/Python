texto = input("Escribe un texto: ")

texto = texto.lower()

contVocales = 0
contEspacios = 0

for vocal in texto:
    vocales = {letra for letra in texto if letra in "aeiou"}
    if len(vocal) >= 1:
        contVocales += 1

print("Numero de vocales: ", contVocales)




