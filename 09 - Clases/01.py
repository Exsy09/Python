class Perro:

    def __init__(self, secreto, secretisimo, nombre="Bobby"):
        self.nombre = nombre
        self._secreto = secreto
        self.__secretisimo = secretisimo

    def llamar(self):
        return "Ey " + self.nombre + " Ven aqui!"

#mascota1 = Perro()
#print(mascota1.llamar())
#mascota2 = Perro("Sultán")
#print(mascota2.llamar())
#mascota1.nombre = "Satán"
#print(mascota1.llamar())

mascota2 = Perro("Bebé", "Chuchillo", "Sia")
print(mascota2.llamar())
mascota2._secreto = "Perro del diablo"
print(mascota2._secreto)
mascota2._Perro__secretisimo = "tusmuertos"
print(mascota2._Perro__secretisimo)