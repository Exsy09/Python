import pickle

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def mostrarDatos(self):
        print("Nombre:", self.nombre, ", Edad:", str(self.edad))

p1 = Persona("Kvothe", 22)
p2 = Persona("Luo Ji", 34)
lista = [p1, p2]

try:
    fichero = open("Persona.bin", "wb")
    pickle.dump(p1, fichero)
    pickle.dump(p2, fichero)
    pickle.dump(lista, fichero)
    fichero.close()

    fichero = open("Persona.bin", "rb")
    persona = pickle.load(fichero)
    persona2 = pickle.load(fichero)
    lista2 = pickle.load(fichero)
    persona.mostrarDatos()
    persona2.mostrarDatos()
    for p in lista2:
        p.mostrarDatos()
    fichero.close()
except:
    print("supuper mamada galaxial xdddd weon")