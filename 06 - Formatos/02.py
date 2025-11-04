lista = ["Ezreal", "Varus", "Aphelios", "Jhin"]
n1 = 23
n2 = 456
n3 = 1
print(f"Numeros: \n{n1:04d}\n{n2:04d}\n{n3:04d}")
print(f"Justificado a la izquierda: ***{n1:<20}***")
print(f"Justificado a la derecha  : ***{n1:>20}***")
print(f"Justificado al centro     : ***{n1:^20}***")
print(f"Inspeccionando variables: {n1=} y {n2=}")
print(f"Inspeccionando variables: {lista=}")

def devuelveMiNombre():
    return "Aitor"

print(f"Mi nombre es: {devuelveMiNombre()}")


campeon = "Ezreal"
posicion = "ADC"
meta = "Sí"

ficha = f"""
Ficha del Campeon
=======================================
Nombre: {campeon}
Rol: {posicion}
Meta: {meta}
=======================================
"""
print(ficha)