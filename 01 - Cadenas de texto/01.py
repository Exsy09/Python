texto = "Hola mundo"
print(len(texto)) # Devuelve la longitud de la cadena
# for c in texto:
#     print(c)

# for i in range(0, len(texto)):
#     print(i, " - ", texto[i]) # Nos devuelve la posicion de cada caracter

print(texto[3:8]) # Me devuelve desde la posicion 3 hasta la 8
print(texto[:8]) # Me devuelve desde el principio a la 8
print(texto[3:]) # Me devuelve desde la 3 hasta el final

print(texto[-2]) # Cuenta al reves, muestra desde atras

cadenaNumerica = str(3456.5) # Permite convertir de numero a cadena tipo String
print(cadenaNumerica)

print(texto.upper()) # Convierte la cadena en MAYUSCULAS, pero no modifica el original
print(texto.lower()) # Convierte la cadena en minusculas
print(texto.swapcase()) # Transforma las minusculas en mayusculas y viceversa

print(texto.find("o")) # Devuelve la primera posicion en la que aparece, si no aparece muestra -1
print(texto[2:].find("o"))
print(texto.count("o")) # Devuelve en numero de veces que aparece en la cadena, si no aparece devuelve 0
print(texto.replace("o", "x")) # Sustituye el primer valor por el segundo
print(texto.replace("o", "x", 1)) # Sustituye solo las veces que ponga en el count
print(texto.replace("o", "0"))