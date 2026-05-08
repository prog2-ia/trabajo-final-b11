class Playlist:
    def __init__(self, nombre_playlist: str) -> None:
            self.nombre_playlist = nombre_playlist
            self.pistas = []

    # Añade una pista a la lista si no estaba
    def añadir_pista(self,pista: ElementoMultimedia) -> None:
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
    def __add__(self, otra_playlist: Self) -> Self:
        nueva = Playlist(f'Mezcla las playlists: {self.nombre_playlist} y {otra_playlist.nombre_playlist}')
        nueva.pistas = self.pistas.copy()
        for pista in otra_playlist.pistas:
            if pista not in nueva.pistas:
                nueva.pistas.append(pista)
        return nueva

    # Compara dos playlists
    def __eq__(self, otra_playlist: Any) -> bool:
        return self.pistas == otra_playlist.pistas
