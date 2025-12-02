class Coleccion:
    def __init__(self, autor, tituloOri, genero, ultimaPubli):
        self.autor = autor
        self.tituloOri = tituloOri
        self.genero = genero
        self.ultimaPubli = ultimaPubli

    @titulo.setter
    def titulo(self, titulo_traducido):
        self.titulo = titulo_traducido

    @ultima.setter
    def ultima(self, ultima_publicacion):
        self.ultima = ultima_publicacion