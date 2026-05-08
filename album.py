from perfiles import Artista
from tipos_audio import Cancion

class Album:
    def __init__(self, titulo: str, año_lanzamiento: int, artista: Artista) -> None:
        self.titulo = titulo
        self.año_lanzamiento = año_lanzamiento
        self.canciones: list[Cancion] = []

        if isinstance(artista, Artista):
            self.artista_creador = artista
        else:
            self.artista_creador = Artista('Artista Desconocido', 'Desconocido')

    def agregar_cancion(self, cancion: Cancion) -> None:
        self.canciones.append(cancion)

    def mostrar_album(self) -> str:
        texto_album = f'Álbum: {self.titulo} ({self.año_lanzamiento}) - Por: {self.artista_creador.nombre}\n'
        texto_album += 'Pistas:\n'
        numero = 1
        for cancion in self.canciones:
            texto_album += f' {numero}. {cancion.titulo}\n'
            numero += 1
        return texto_album