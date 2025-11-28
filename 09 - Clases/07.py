# pokemonDragon = ["Hydreigon", "Haxorus", "Salamance"]
# iterador = iter(pokemonDragon)
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
#print(next(iterador, "NO HAY MAS DRAGONES"))
from time import sleep


class diasDeLaSemana:
    def __init__(self, dia):
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.indice = dia


    def mostrarDia(self):
        print(self.dias[self.indice])

    def __iter__(self):
        return self # devuelve el mismo objeto

    def __next__(self):
        dia_actual = self.dias[self.indice]
        if self.indice == len(self.dias)-1:
            self.indice = 0
        else:
            self.indice +=1
        return dia_actual # hace que de una lista printee lo dias y cuando llegue al ultimo y vualve a empezar

dia = diasDeLaSemana(2)
dia.mostrarDia()

iterador = iter(dia)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))