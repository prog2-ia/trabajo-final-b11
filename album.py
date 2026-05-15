from perfiles import Artista
from tipos_audio import Cancion

class Album:
    def __init__(self, titulo: str, año_lanzamiento: int, artista: Artista) -> None:
        #Impedimos que el nombre del álbum esté vacío
        if not titulo.strip():
            raise ValueError('Título no válido, no puede estar vacío')

        #Impedimos que se añada un año de lanzamiento negativo o mayor que el año actual
        if año_lanzamiento < 0 or año_lanzamiento > 2026:
            raise ValueError('Año de lanzamiento inválido; debe estar entre 0 y 2026')

        self.titulo = titulo.strip()
        self.año_lanzamiento = año_lanzamiento
        self.canciones: list[Cancion] = []

        #Añadimos un manejo de excepciones en caso de que el tipo de dato sea
        #incorrecto para el parámetro "artista"
        if not isinstance(artista, Artista):
            raise TypeError('Artista no válido, se esperaba una instancia de "Artista"')

        self.artista_creador = artista

    def __iadd__(self, cancion: Cancion) -> 'Album':
        # Podemos añadir canciones coon +=
        if not isinstance(cancion, Cancion):
            raise TypeError('Solo puedes sumar objetos de tipo Cancion')
        if cancion in self.canciones:
            raise ValueError('La canción ya está en el álbum')
        else:
            self.canciones.append(cancion)
        return self

    def __isub__(self, cancion: Cancion) -> 'Album':
        # Podemos eliminar canciones con -=
        if cancion in self.canciones:
            self.canciones.remove(cancion)
        else:
            raise ValueError('La canción a eliminar no está en el álbum')
        return self


    def mostrar_album(self) -> str:
        texto_album = f'Álbum: {self.titulo} ({self.año_lanzamiento}) - Por: {self.artista_creador.nombre}\n'
        texto_album += 'Pistas:\n'
        numero = 1
        for cancion in self.canciones:
            texto_album += f' {numero}. {cancion.titulo}\n'
            numero += 1
        return texto_album
