import random


class Pokemon:
    # Lista de tipos permitidos
    TIPOS_VALIDOS = [
        "Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha", "Veneno",
        "Eléctrico", "Tierra", "Roca", "Psíquico", "Hielo", "Bicho",
        "Fantasma", "Dragón"
    ]
    NOMBRES_VALIDOS = [
          "Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard",
          "Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree",
          "Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot",
          "Rattata","Raticate","Spearow","Fearow","Ekans","Arbok",
          "Pikachu","Raichu","Sandshrew","Sandslash","Nidoran♀","Nidorina",
          "Nidoqueen","Nidoran♂","Nidorino","Nidoking","Clefairy","Clefable",
          "Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat",
          "Oddish","Gloom","Vileplume","Paras","Parasect","Venonat",
          "Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck",
          "Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag",
          "Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop",
          "Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool",
          "Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash",
          "Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo",
          "Dodrio","Seel","Dewgong","Grimer","Muk","Shellder",
          "Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee",
          "Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute",
          "Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung",
          "Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela",
          "Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu",
          "Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar",
          "Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto",
          "Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte",
          "Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno",
          "Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"
    ]


    def __init__(self, codigo, nombre, tipo1, tipo2, evolucion = None):
        # Validar código (1 a 151)
        if not (1 <= codigo <= 151):
            raise ValueError("El código debe estar entre 1 y 151.")

        # Validar nombre
        if nombre not in Pokemon.NOMBRES_VALIDOS:
            raise ValueError("Este pokemon no pertence a esta generación")

        # Validar tipo
        if tipo2 == "null":
            tipo2 = ""
        elif tipo1 not in Pokemon.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido. Tipos permitidos: {Pokemon.TIPOS_VALIDOS}")
        elif tipo2 not in Pokemon.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido. Tipos permitidos: {Pokemon.TIPOS_VALIDOS}")

        self.codigo = codigo
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.evolucion = evolucion
        self.vida = random.randint(50, 100)

    def mostrar_info(self):
        print(f"Pokémon #{self.codigo}: {self.nombre} - {self.tipo1} {self.tipo2} - {self.vida}")

    def evolucionar(self):
        if self.evolucion is None:
            print(f"{self.nombre} no tiene evolución.")
            return self
        else:
            print(f"{self.nombre} está evolucionando en {self.evolucion}")
            return self.evolucion

    def combateContra(self, rival):
        damage = random.randint(25, 100)
        rival.vida -= damage
        if rival.vida != 0:
            damage = random.randint(25, 100)
            self.vida -= damage
            if self.vida <= 0:
                print(f"{self.nombre} ha sido derrotado")
            else:
                print("Sigue el combate")
        else:
            print(f"{rival.nombre} ha sido derrotado")

"""
pikachu = Pokemon(25, "Pikachu", "Electrico", "null", "Raichu")
pikachu.mostrar_info()
pikachu.evolucionar()

tentacruel = Pokemon(73, "Tentacruel", "Agua", "Veneno")
tentacruel.mostrar_info()
tentacruel.evolucionar()


hydreigon = Pokemon(35, "Hydreigon", "Dragón", "Siniestro")
hydreigon.mostrar_info()
hydreigon.evolucionar()
"""
pikachu = Pokemon(25, "Pikachu", "Electrico", "null", "Raichu")
nidoking = Pokemon(34, "Nidoking", "Veneno", "Tierra")
nidoking.combateContra(pikachu)
pikachu.mostrar_info()
nidoking.mostrar_info()
