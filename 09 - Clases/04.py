class Pokemon:

    def __init__(self, nombre, nivel):
        self.__nombre = []
        self.__nombre.append(nombre)
        self.__nivel = nivel

    @property
    def nombre(self):
        return (self.__nombre)
    @property
    def nivel(self):
        return self.__nivel

    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    @nivel.setter
    def nivel(self, nuevoNivel):
        self.__nivel = nuevoNivel

    def __add__(self, Pokemon):
        self.__nivel = self.__nivel + Pokemon.__nivel
        self.__nombre = self.__nombre + Pokemon.__nombre
        return self

p1 = Pokemon("Hydreigon", 89)
p2 = Pokemon("Haxorus", 67)
p1 = p1 + p2

print(p1.nombre)
print(p1.nivel)
