from enum import Enum


# =========================
# ENUMERACIÓN DE GÉNEROS
# =========================

class Genero(Enum):
    SHONEN = "Shonen"
    SHOJO = "Shojo"
    SEINEN = "Seinen"
    JOSEI = "Josei"
    KODOMO = "Kodomo"
    YURI = "Yuri"
    SPOKON = "Spokon"
    ISEKAI = "Isekai"
    HENTAI = "Hentai"


# =========================
# CLASE MANGA
# =========================

class Manga:
    def __init__(self, mangaka, titulo_japones, genero, ultimo_numero_publicado, titulo_espanol=None):
        self.__mangaka = mangaka
        self.__titulo_japones = titulo_japones
        self.__titulo_espanol = titulo_espanol
        self.__genero = genero
        self.__ultimo_numero_publicado = ultimo_numero_publicado
        self.__numeros_que_tengo = set()

    # =========================
    # GETTERS
    # =========================

    def get_mangaka(self):
        return self.__mangaka

    def get_titulo_japones(self):
        return self.__titulo_japones

    def get_titulo_espanol(self):
        return self.__titulo_espanol

    def get_genero(self):
        return self.__genero

    def get_ultimo_numero_publicado(self):
        return self.__ultimo_numero_publicado

    def get_numeros_que_tengo(self):
        return sorted(self.__numeros_que_tengo)

    # =========================
    # SETTERS
    # =========================

    def set_titulo_espanol(self, titulo_espanol):
        self.__titulo_espanol = titulo_espanol

    def set_ultimo_numero_publicado(self, numero):
        if numero < self.__ultimo_numero_publicado:
            print("⚠️ El último número publicado no puede ser menor al actual.")
        else:
            self.__ultimo_numero_publicado = numero

    # =========================
    # MÉTODOS DE GESTIÓN
    # =========================

    def comprar_numeros(self, *numeros):
        for numero in numeros:
            if numero in self.__numeros_que_tengo:
                print(f"⚠️ Ya tienes el número {numero}.")
            elif numero <= 0:
                print(f"⚠️ Número inválido: {numero}.")
            else:
                self.__numeros_que_tengo.add(numero)

    def eliminar_numero(self, numero):
        if numero in self.__numeros_que_tengo:
            self.__numeros_que_tengo.remove(numero)
        else:
            print(f"⚠️ No puedes eliminar el número {numero} porque no lo tienes.")

    def numeros_que_faltan(self):
        todos = set(range(1, self.__ultimo_numero_publicado + 1))
        faltan = todos - self.__numeros_que_tengo
        return sorted(faltan)

    # =========================
    # REPRESENTACIÓN
    # =========================

    def __str__(self):
        titulo_es = self.__titulo_espanol if self.__titulo_espanol else "No disponible"
        return (
            f"Manga: {self.__titulo_japones}\n"
            f"Título en español: {titulo_es}\n"
            f"Mangaka: {self.__mangaka}\n"
            f"Género: {self.__genero.value}\n"
            f"Último número publicado: {self.__ultimo_numero_publicado}\n"
            f"Números que tengo: {self.get_numeros_que_tengo()}"
        )


# =========================
# EJEMPLO DE USO
# =========================

if __name__ == "__main__":
    manga = Manga(
        mangaka="Eiichiro Oda",
        titulo_japones="One Piece",
        titulo_espanol="One Piece",
        genero=Genero.SHONEN,
        ultimo_numero_publicado=108
    )

    manga.comprar_numeros(1, 2, 3, 5, 8)
    manga.comprar_numeros(3, 5)      # Repetidos
    manga.eliminar_numero(4)         # No lo tengo
    manga.eliminar_numero(2)

    print(manga)
    print("Números que faltan:", manga.numeros_que_faltan())
