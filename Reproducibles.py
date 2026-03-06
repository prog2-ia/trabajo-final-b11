class ElementoMultimedia:
    def __init__(self,titulo,duracion,fecha_lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.fecha_lanzamiento=fecha_lanzamiento
    def mostrar(self):
       print(f'Estas reproduciendo {titulo} lanzada el {fecha_lanzamiento} y de duracion {duracion}')

class Cancion(ElementoMultimedia):
    def __init__(self,titulo,duracion,fecha_lanzamiento,artista,album,genero):
        super().__init__(titulo, duracion, fecha_lanzamiento)
        self.artista = artista
        self.album = album
        self.genero = genero
    def mostrar(self):
        super().mostrar()
        print(f'Del artista {artista} y el album {album}, Genero: {genero}')

class Podcast(ElementoMultimedia):
    def __init__(self,titulo,duracion,fecha_lanzamiento,presentador,num_episodio,tema):
        super().__init__(titulo, duracion, fecha_lanzamiento)
        self.presentador = presentador
        self.num_episodio = num_episodio
        self.tema = tema
    def mostrar(self):
        super().mostrar()
        print(f'Episodio {num_episodio} sobre {tema} del presentador {presentador}')



