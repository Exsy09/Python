class Siniestro:
    def __init__(self):
        self.nombre = "Siniestro"

    def getNombre(self):
        return self.nombre


class Fantasma(Siniestro):
    def __init__(self):
        self.nombre = "Fantasma"


objetoA = Siniestro()
objetoB = Fantasma()

print(objetoA.getNombre())
print(objetoB.getNombre())

class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"
        self.codigo = 55

    def cambiarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre


class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()
        self.subclase = "Clase B"

    def incrementaCodigo(self):
        self.codigo += 1

objetoA = ClaseA()
objetoB = ClaseB()

print(objetoA.cambiarNombre())
print(objetoB.cambiarNombre())
print(objetoB.subclase)