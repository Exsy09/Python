diccionario = {"Nombre": "Sara", "Edad": 57, "Solterx": True, "Edad": 33} # No permite duplicados, asi que guarda el ultimo

print(diccionario)
print(diccionario["Edad"])
print(diccionario.get("Edad")) # devuelve lo mismo, pero con un metrodo

for elemento in diccionario:
    print(elemento) # devuelve el nombre de cada elemento

for elemento in diccionario:
    print(diccionario[elemento]) # devuelve el valor del elemento

for elemento in diccionario:
    print(elemento, ":", diccionario[elemento]) # devuelve ambos

for clave, valor in diccionario.items():
    print(clave, ":", valor) # otra manera del anterior

diccionario["Edad"] = 44 #Modifica el campo en cuestion
print(diccionario["Edad"])
# diccionario.clear() # Borra todo el contenido del diccionario

dicc2 = dict(Primero = 'Uno', Tercero = 'Tres')


