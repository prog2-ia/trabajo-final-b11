from elemento_multimedia import ElementoMultimedia
from typing import Any

class Playlist:
    def __init__(self, nombre_playlist: str) -> None:
            # El nombre de la playlist no puede estar vacío
            if not nombre_playlist.strip():
                raise TypeError('Nombre de la playlist inválido, no puede estar vacío')
            self.nombre_playlist = nombre_playlist
            self.pistas = list[ElementoMultimedia] = []

    # Añade una pista a la lista si no estaba
    def añadir_pista(self,pista: ElementoMultimedia) -> None:
        # Impedir que se añada una pista que no sea de tipo ElementoMultimedia
        if not isinstance(pista, ElementoMultimedia):
            raise TypeError('Sólo pueden añadirse objetos de tipo ElementoMultimedia')
        if pista not in self.pistas:
            self.pistas.append(pista)

    # Elimina una pista de la lista si estaba
    def eliminar_pista(self,pista:ElementoMultimedia) -> None:
        if pista in self.pistas:
            self.pistas.remove(pista)

    def calcular_duracion_playlist(self) -> int:
        duracion_t = 0
        for cancion in self.pistas:
            duracion_t += cancion.duracion
        return duracion_t

    def mostrar_playlist(self) -> str:
        if not self.pistas:
            return f'Nombre de la playlist: {self.nombre_playlist}\n no tiene contenido.'
        pistas_playlist=''
        for pista in self.pistas:
            pistas_playlist += f'{pista.mostrar()}\n'
        return f'Nombre de la playlist: {self.nombre_playlist}\n Canciones: \n{pistas_playlist}'

    # Mezcla dos playlists sin duplicados
    def __add__(self, otra_playlist: 'Playlist') -> 'Playlist':
        # Como en anteriores ejemplos, impedimos datos que no sean los
        # buscados, en este caso Playlist:
        if not isinstance(otra_playlist, Playlist):
            raise TypeError('El tipo de dato debe ser Playlist"')
        nueva = Playlist(f'Mezcla las playlists: {self.nombre_playlist} y {otra_playlist.nombre_playlist}')
        nueva.pistas = self.pistas.copy()
        for pista in otra_playlist.pistas:
            if pista not in nueva.pistas:
                nueva.pistas.append(pista)
        return nueva

    # Compara dos playlists
    def __eq__(self, otra_playlist: Any) -> bool:
        # Si no es una playlist, el mét.odo no puede compararlas
        if not isinstance(otra_playlist, Playlist):
            return False
        return self.pistas == otra_playlist.pistas
