from playlist import Playlist

class Biblioteca:
    def __init__(self, nombre_biblioteca: str) ->None:
        self.nombre = nombre_biblioteca
        self.catalogo = []
        self.playlists = []

    def agregar_al_catalogo(self, elemento: ElementoMultimedia) -> str:
        self.catalogo.append(elemento)
        return f'{elemento.titulo} se ha añadido al catálogo general.'

    def crear_playlist(self, nombre_playlist: str) -> Playlist:
        nueva_playlist = Playlist(nombre_playlist)
        self.playlists.append(nueva_playlist)
        return nueva_playlist

    def mostrar_catalogo(self) -> str:
        elementos_biblioteca=''
        for elemento in self.catalogo:
            elementos_biblioteca += f'{elemento.mostrar()}\n'
        return elementos_biblioteca