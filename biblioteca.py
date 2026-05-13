from playlist import Playlist
from elemento_multimedia import ElementoMultimedia

class Biblioteca:
    def __init__(self, nombre_biblioteca: str) ->None:
        if not nombre_biblioteca.strip():
            raise ValueError('El nombre de la biblioteca es inválido, no puede estar vacío')
        self.nombre = nombre_biblioteca
        self.catalogo = list[ElementoMultimedia] = []
        self.playlists = list[Playlist] = []

    def agregar_al_catalogo(self, elemento: ElementoMultimedia) -> str:
        self.catalogo.append(elemento)
        return f'{elemento.titulo} se ha añadido al catálogo general.'

    def crear_playlist(self, nombre_playlist: str) -> Playlist:
        nueva_playlist = Playlist(nombre_playlist)
        self.playlists.append(nueva_playlist)
        return nueva_playlist

    def mostrar_catalogo(self) -> str:
        if not self.catalogo:
            raise ValueErrpr('La biblioteca está vacía')
        elementos_biblioteca=''
        for elemento in self.catalogo:
            elementos_biblioteca += f'{elemento.mostrar()}\n'
        return elementos_biblioteca
