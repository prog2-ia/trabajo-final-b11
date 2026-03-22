from abc import ABC, abstractmethod

class ElementoMultimedia(ABC):
    def __init__(self,titulo:str,duracion,fecha_lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.fecha_lanzamiento = fecha_lanzamiento

@property
def duracion(self):
    return self._duracion

@duracion.setter
def duracion(self, valor):
    if valor <= 0:
        self._duracion = 3.0
    else:
        self._duracion = valor

@abstractmethod
def mostrar(self):
    return f'Estas reproduciendo {self.titulo} lanzada el {self.fecha_lanzamiento} y de duracion {self.duracion}'

def __eq__(self, otro):
    if isinstance(otro, ElementoMultimedia):
        return self.titulo == otro.titulo and self.duracion == otro.duracion
    else:
        return False

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

class Playlist:
    def __init__(self,nombre_playlist):
        self.nombre_playlist=nombre_playlist
        self.pistas=[]

def añadir_pista(self,pista):
    if pista not in self.pistas:
        self.pistas.append(pista)

def eliminar_pista(self,pista):
    if pista in self.pistas:
        self.pistas.remove(pista)

def calcular_duracion_playlist(self):
    duracion_t = 0
        for cancion in self.pistas:
        duracion_t+=cancion.duracion
        return duracion_t

def mostrar_playlist(self):
    if not self.pistas:
            return f'Nombre de la playlist: {self.nombre_playlist}\n no tiene contenido.'

    pistas_playlist=''
    for pista in self.pistas:
        pistas_playlist+=f'{pista.mostrar()}\n'
        return f'Nombre de la playlist: {self.nombre_playlist}\n Canciones: \n{pistas_playlist}'

def __add__(self, otra_playlist):
    nueva = Playlist(f'Mezcla las playlists: {self.nombre_playlist} y {otra_playlist.nombre_playlist}')
    nueva.pistas = self.pistas.copy()
    for pista in otra_playlist.pistas:
        if pista not in nueva.pistas:
            nueva.pistas.append(pista)
            return nueva

def __eq__(self, otra_playlist):
    return self.pistas == otra_playlist.pistas

class Biblioteca:
    def __init__(self, nombre_biblioteca):
        self.nombre = nombre_biblioteca
        self.catalogo = []
        self.playlists = []

def agregar_al_catalogo(self, elemento):
    self.catalogo.append(elemento)
    return f'{elemento.titulo} se ha añadido al catálogo general.'

def crear_playlist(self, nombre_playlist: str):
    nueva_playlist = Playlist(nombre_playlist)
    self.playlists.append(nueva_playlist)
    return nueva_playlist

def mostrar_catalogo(self):
    elementos_biblioteca=''
    for elemento in self.catalogo:
        elementos_biblioteca += f'{elemento.mostrar()}\n'
        return elementos_biblioteca