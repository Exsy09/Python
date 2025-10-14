adcarry = {"Ezreal", "Varus", "Caitlyn", "Jhin", "Draven", "Yunara", "Corki"}
print(adcarry)

midlaner = set(["Ahri", "Azir", "Orianna", "Sylas", "Syndra", "Talon", "Corki"])
print(midlaner)

if "Ezreal" in adcarry:
    print("Ezreal es adc")
if "Azir" not in adcarry:
    print("Azir no es adc")

for elemento in adcarry:
    print(elemento)

print(len(adcarry))

for i in range(0, len(adcarry)):
    # print(adcarry[i])
    print("HOLa")

# Añadir elementos
adcarry.add("Ashe")
print(adcarry)
midlaner.add("Lissandra")
print(midlaner)

# Eliminar elementos
adcarry.remove("Draven")
print(adcarry)
midlaner.remove("Syndra")
print(midlaner)

#Alternativa de remove (no da error cuando el elemento no existe)
adcarry.discard("Draven")
print(adcarry)

# Elige un elemento "aleatorio" (el primero del conjunto)
adc = adcarry.pop()
print(adc)

# Elimina el conjunto completoa
adcarry.clear()
print(adcarry)


conjunto1 = set([1,3,3,4,5,6,2,3,4,5,6]) # Elimina los duplicados
print(conjunto1)
conjunto2 = set("Hola mundo cruel")
print(conjunto2) # Elimina caracteres duplicados

lista = list(midlaner) # Convierte en lista
print(lista)
tupla = tuple(midlaner) # Convierte en tupla
print(tupla)
texto = str(midlaner) # Convierte en texto
print(texto)

print(adcarry | midlaner) # Union, sin duplicados
print(adcarry & midlaner) # Intersección
print(adcarry - midlaner) # Diferencia
print(adcarry ^ midlaner) # Exclusive OR

print(adcarry.union(midlaner)) # Union, sin duplicados
print(adcarry.intersection(midlaner)) # Intersección
print(adcarry.difference(midlaner)) # Diferencia
print(adcarry.symmetric_difference(midlaner)) # Exclusive OR