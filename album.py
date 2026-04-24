from perfiles import Artista


class Album:
    def __init__(self, titulo, año_lanzamiento, artista):
        self.titulo = titulo
        self.año_lanzamiento = año_lanzamiento
        self.canciones = []

        if isinstance(artista, Artista):
            self.artista_creador = artista
        else:
            self.artista_creador = Artista('Artista Desconocido', 'Desconocido')

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def mostrar_album(self):
        texto_album = f'Álbum: {self.titulo} ({self.año_lanzamiento}) - Por: {self.artista_creador.nombre}\n'
        texto_album += 'Pistas:\n'
        numero = 1
        for cancion in self.canciones:
            texto_album += f' {numero}. {cancion.titulo}\n'
            numero += 1
        return texto_album