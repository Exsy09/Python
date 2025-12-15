tupla = (1,2,3,4,5)
print(tupla)
tupla2 = ("Ezreal", "Hecarim", "Ryze")
print(tupla2)
tupla3 = (23, "Warwick", False, (1,2,3), 44.5, [1,2,3])
print(tupla3)
tupla4 = ()
print(tupla4)
tupla5 = ("Jonia",) # Para que detecte que es de un solo elemento, si no, considera que es un string o un num
print(tupla5)

lista = list(tupla2)
print(lista) # Convierte la tupla en una lista, para poder modificar la tupla

texto = str(tupla2)
print(texto) # Convierte la tupla en un String

tupla6 = tuple([1,2,3,4,5])
print(tupla6) # Convierte la lista en una tupla
tupla7 = tuple("Hola mundo")
print(tupla7) # Convierte el string en un tupla

tupla8 = "Alistar", "Braum", "Nautilus"
print(tupla8)

if 2 in tupla:
    print("El 2 está en la tupla")
if 33 not in tupla:
    print("El 33 no está en la tupla")

profesor = ("Jose Maria", "Morales", 57, False, True)
nombre, apellido, edad, alumno, profesor = profesor
print(apellido, edad)
