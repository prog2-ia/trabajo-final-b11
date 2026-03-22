from elemento_multimedia import ElementoMultimedia

class Cancion(ElementoMultimedia):
    def __init__(self,titulo,duracion,fecha_lanzamiento,artista,album,genero):
        super().__init__(titulo, duracion, fecha_lanzamiento)
        self.artista = artista
        self.album = album
        self.genero = genero

    def mostrar(self):
        mostrar_elemento=super().mostrar()
        return f'{mostrar_elemento} del artista {self.artista} y el album {self.album}. Genero: {self.genero}'

class Podcast(ElementoMultimedia):
    def __init__(self,titulo,duracion,fecha_lanzamiento,presentador,num_episodio,tema):
        super().__init__(titulo, duracion, fecha_lanzamiento)
        self.presentador = presentador
        self.num_episodio = num_episodio
        self.tema = tema

    def mostrar(self):
        mostrar_elemento=super().mostrar()
        return f'{mostrar_elemento} episodio {self.num_episodio} sobre {self.tema} del presentador {self.presentador}'