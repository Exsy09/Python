d1 = {}
d2 = dict()
d3 = {"Nombre": "Ezreal", "Rol": "ADC", "Daño AD": True, "Daño AP": True, "Nota": 10}
d4 = dict(Primero = 'uno', Tercero = 'tres')

print(d3.get("Titulo")) # devuelve 'None' si no lo encuentra
print(d3.pop("Nota")) # devuelve el valor que elimina (el ultimo insertado)
print(d3.popitem()) # devuelve una tupla y elimina los datos del diccionario que forman la tupla
d3.update(d4) # añade al diccionario d3 los elementos de d4
print(d3)