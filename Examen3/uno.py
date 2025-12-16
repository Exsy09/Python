from more_itertools.more import nth_combination_with_replacement


class Vehiculo():
    def __init__(self, matricula, añoCompra):
        self.matricula = matricula
        self.añoCompra = añoCompra

class Coche(Vehiculo):

    def __init__(self, matricula, añoCompra):
        super().__init__(matricula, añoCompra)
        self.nombre = "Jose María Morales"
        self.edad = 57
        self.añoCarnet = 39
        self.puntos = 10

    def todoRiesgo(self):
        if self.añoCompra == 2025:
            print("Precio del seguro a todo riesgo: 400€")
        elif self.añoCompra == 2025 and self.puntos < 8:
            print("Precio del seguro a todo riesgo: 500€")
        elif self.añoCompra == 2024:
            print("Precio del seguro a todo riesgo: 500€")
        elif self.añoCompra == 2024 and self.puntos < 8:
            print("Precio del seguro a todo riesgo: 600€")
        elif self.añoCompra == 2023:
            print("Precio del seguro a todo riesgo: 700€")
        elif self.añoCompra == 2023 and self.puntos < 8:
            print("Precio del seguro a todo riesgo: 800€")
        elif self.añoCompra < 2023:
            print("Precio del seguro a todo risego:", 250*(2026 - self.añoCompra), "€")
        elif self.añoCompra < 2023 and self.puntos < 8:
            print("Precio del seguro a todo risego:", 250*(2026 - self.añoCompra), "€")
        else:
            print("No se puede calcular")

    def terceros(self):
        self.precio = 250
        if self.puntos < 8:
            self.precio = self.precio + 100
        elif self.edad < 24:
            self.precio = self.precio + 50
        elif self.añoCarnet < 2:
            self.precio = self.precio + 75

        print("Precio del seguro a terceros:", self.precio, "€")

    def info(self):
        print("Vehiculo: coche", "Matricula:", self.matricula, "Año de compra:", self.añoCompra, "\nConductor:", self.nombre, "Edad:", self.edad, "Años de carnet:", self.añoCarnet, "Puntos:", self.puntos)

class Moto(Vehiculo):
    def __init__(self, matricula, añoCompra):
        super().__init__(matricula, añoCompra)
        self.nombre = "Inés Perado"
        self.edad = 18
        self.añoCarnet = 1
        self.puntos = 8

    def terceros(self):
        self.precio = 200
        if self.puntos < 8:
            self.precio = self.precio + 150
        elif self.edad < 24:
            self.precio = self.precio + 25
        elif (self.añoCarnet - 2026) < 2:
            self.precio = self.precio + 50

        print("Precio del seguro a terceros:", self.precio, "€")

    def todoRiesgo(self):
        print("No se hacen seguros todo riesgo de motos.")

    def info(self):
        print("Vehiculo: moto", "Matricula:", self.matricula, "Año de compra:", self.añoCompra)





miCoche = Coche(6310, 2024)
miCoche.info()
miCoche.todoRiesgo()
miCoche.terceros()

miMoto = Moto(6309, 2025)
miMoto.info()
miMoto.todoRiesgo()
miMoto.terceros()
