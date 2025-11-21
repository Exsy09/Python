class Pokemon:
    numPokemon = 0
    def __init__(self, nombre = "Bisharp"):
        self.nombre = nombre
        Pokemon.numPokemon += 1

    def llamar(self):
        return self.nombre, " !Yo te elijo!"

    def cuantosPokemon(self):
        return Pokemon.numPokemon

    @classmethod
    def cuantosPokemon2(cls):
        return cls.numPokemon

    @staticmethod
    def rugir():
        return "fkrgwer"

    def sobrecargada(self, atributo):
        if isinstance(atributo, int):
            print("Estoy trabajando con entero")
        elif isinstance(atributo, float):
            print("Ahora con float")
        elif isinstance(atributo, str):
            print("Ahora string")
        elif isinstance(atributo, list):
            print("Con lista")

    def sobrecargada2(self, *atributos):
        if len(atributos) == 1:
            print("Recibo un parametro")
        elif len(atributos) == 2:
            print("Recibo dos parametros")
        else:
            print("Recibo mas de dos parametros")

Pokemon1 = Pokemon("Pikachu")
Pokemon2 = Pokemon()
Pokemon3 = Pokemon("Deino")

print(Pokemon1.cuantosPokemon())
print(Pokemon3.cuantosPokemon())
print(Pokemon2.cuantosPokemon())

print(Pokemon.cuantosPokemon2())
print(Pokemon.rugir())
print(Pokemon3.rugir())

Pokemon3.sobrecargada(3)
Pokemon3.sobrecargada(3.5)
Pokemon3.sobrecargada("hola")
Pokemon3.sobrecargada([1,2,3])

Pokemon3.sobrecargada2(1, [4,8],2)