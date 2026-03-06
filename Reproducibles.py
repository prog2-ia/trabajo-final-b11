class ElementoMultimedia:
    def __init__(self,titulo,duracion,fecha_lancamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.fecha_lanzamiento=fecha_lanzamiento

class Cancion(ElementoMultimedia):
    def __init__(self,titulo,duracion,fecha_lanzamiento,artista,album,genero):
        super().__init__(titulo, duracion, fecha_lanzamiento)
        self.artista = artista
        self.album = album
        self.genero = genero
class Podcast(ElementoMultimedia):
    def __init__(self,titulo,duracion,fecha_lanzamiento,presentador,num_episodio,tema):
        super().__init__(titulo, duracion, fecha_lanzamiento)
        self.presentador=presentador
        self.num_episodio=num_episodio
        self.tema=tema




