class ElementoMultimedia:
    def __init__(self,titulo,duracion,fecha_lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.fecha_lanzamiento=fecha_lanzamiento
    def mostrar(self):
       print(f'Estas reproduciendo {self.titulo} lanzada el {self.fecha_lanzamiento} y de duracion {self.duracion}')

class Cancion(ElementoMultimedia):
    def __init__(self,titulo,duracion,fecha_lanzamiento,artista,album,genero):
        super().__init__(titulo, duracion, fecha_lanzamiento)
        self.artista = artista
        self.album = album
        self.genero = genero
    def mostrar(self):
        super().mostrar()
        print(f'Del artista {self.artista} y el album {self.album}, Genero: {self.genero}')

class Podcast(ElementoMultimedia):
    def __init__(self,titulo,duracion,fecha_lanzamiento,presentador,num_episodio,tema):
        super().__init__(titulo, duracion, fecha_lanzamiento)
        self.presentador = presentador
        self.num_episodio = num_episodio
        self.tema = tema
    def mostrar(self):
        super().mostrar()
        print(f'Episodio {self.num_episodio} sobre {self.tema} del presentador {self.presentador}')
class Playlist:
    def __init__(self,nombre_playlist):
        self.nombre_playlist=nombre_playlist
        self.pistas=[]
    def añadir_pista(self,pista):
        self.pistas.append(pista)
    def eliminar_pista(self,pista):
        self.pistas.remove(pista)
    def calcular_duracion_playlist(self):
        duracion_t=0
        for cancion in self.pistas:
            duracion_t+=cancion.duracion
        return duracion_t
    def mostrar_playlist(self):
        print(f'Nombre de la playlist: {self.nombre_playlist}')
        for pista in self.pistas:
            pista.mostrar_info()








