from playlist import Playlist
from elemento_multimedia import ElementoMultimedia

class Biblioteca:
    def __init__(self, nombre_biblioteca: str) ->None:
        if not nombre_biblioteca.strip():
            raise TypeError('El nombre de la biblioteca es inválido, no puede estar vacío')
        self.nombre = nombre_biblioteca
        self.catalogo = []
        self.playlists = []

    def agregar_al_catalogo(self, elemento: ElementoMultimedia) -> str:
        # Impedir que se añada una pista que no sea de tipo ElementoMultimedia
        if not isinstance(elemento, ElementoMultimedia):
            raise TypeError('Sólo pueden añadirse objetos de tipo ElementoMultimedia')
        self.catalogo.append(elemento)
        return f'{elemento.titulo} se ha añadido al catálogo general.'

    def crear_playlist(self, nombre_playlist: str) -> Playlist:
        # Impedir que se añada una pista que no sea de tipo Playlist
        if not isinstance(nombre_playlist, Playlist):
            raise TypeError('Sólo pueden añadirse objetos de tipo Playlist')
        nueva_playlist = Playlist(nombre_playlist)
        self.playlists.append(nueva_playlist)
        return nueva_playlist

    def mostrar_catalogo(self) -> str:
        elementos_biblioteca=''
        for elemento in self.catalogo:
            elementos_biblioteca += f'{elemento.mostrar()}\n'
        return elementos_biblioteca