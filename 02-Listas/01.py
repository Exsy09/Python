lista = []
lista2 = list()
lista3 = [2, 5, 6, 7, 8, 12]
lista4 = [34, "Pepe", False, 7654.34, [1, 2, 3]] # Puedo listar cualquier tipo de dato, y me lo imprime tal cual está escrito
print(lista4)

for elemento in lista4:
    print(elemento) # Devuelve cada elemento de la lista4

for posicion in range(0, len(lista4)):
    print(posicion, "-", lista4[posicion]) # Devuelve la posicion y el elemento que se encuentra en esa posicion

lista4.append("Nuevo elemento") # Mete un nuevo elemento al final de la lista
print(lista4)

lista5 = lista3 + [23, 45] # Crea una lista con los nuevos elementos sumados al final
print(lista5)

lista6 = lista5 + lista4 # Suma las dos listas para hacer una
print(lista6)

print(lista3)
print(lista3.pop(1)) # Extrae el elemento de la posicion que especifiques

print(lista3)
print(lista3.remove(7)) # Extrae el primer elemento que sea un 7

print(lista3)
lista3.sort()
print(lista3) # Ordena la lista, solo numeros y cadenas

print(lista3)
lista3.sort(reverse=True) # Ordena invertido
print(lista3)