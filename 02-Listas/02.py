lista1 = [1,1,2,3,5,8,13,21,34,55,79]
lista2 = ["Ezreal", "Jhin"]
texto = str(lista1) # Conveirte la lista en string
print(texto)
texto = texto.replace("[","")
texto = texto.replace("]", "")
texto2 = "Hola Mundo"
lista3 = list(texto2) # Hace que un string se convierta en lista
print(lista3)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz[1][0])

print(lista1)
print(lista1[:5]) # Va desde el inicio hasta la posicion (no incluida)
print(lista1[2:5]) # Desde la posicion 1 hasta la 5
print(lista1[5:]) # Desde la posicion 5 hasta el final
print(lista1[5::2]) # Devuelve desde la posicion 5 hasta el final haciendo saltos de 2
print(lista1[::-1]) # Devuelve la lista invertida