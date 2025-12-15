"""
class Entrnador:
    pass

entrenador1 = Entrnador()
entrenador1.nombre = "Ash"
entrenador1.apellidos = "Ketchum"
entrenador1.edad = 15
entrenador1.activo = True

print(entrenador1.apellidos, entrenador1.nombre)
"""

class Entrenador:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.__edad = edad # __ protege el dato

    @property
    def edad(self):
        return (self.__edad)

    @edad.setter
    def edad(self, nuevaEdad):
        self.__edad = nuevaEdad

    def __str__(self):
        return (self.__apellidos + ", " + self.__nombre)


ent1 = Entrenador("Ash", "Ketchum", 15)
print(ent1.edad)
ent1.edad = 16
print(ent1.edad)
print(str(ent1))
"""
x = 5
print(x)
del x # del elimina un elemento y evita que se pueda usar a partir de esa linea
print(x)
"""