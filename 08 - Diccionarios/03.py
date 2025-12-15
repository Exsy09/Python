import random

d1 = dict(Ezreal = 10, Aatrox = 8, Caitlyn = 7, Jhin = 8, Viktor = 7, Lux = 6, Garen = 4)

def eliminarAlAzar(d1):
    claves = list() # creamos una lista vacia
    for elemento in d1:
        claves.append(elemento) # añadimos los elementos a la lista
    d1.pop(random.choice(claves)) # eliminamos al azar un elemento del diccionario
    return d1
print(eliminarAlAzar(d1)) # llamamos a la funcion