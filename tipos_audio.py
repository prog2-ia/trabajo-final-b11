from elemento_multimedia import ElementoMultimedia

class Cancion(ElementoMultimedia):
    def __init__(self, titulo: str, duracion: int, fecha_lanzamiento: int, artista: str, album: str, genero: str) -> None:
        super().__init__(titulo, duracion, fecha_lanzamiento)
        self.artista = artista
        self.album = album
        self.genero = genero

    def mostrar(self) -> str:
        mostrar_elemento = super().mostrar()
        return f'{mostrar_elemento} del artista {self.artista} y el album {self.album}. Genero: {self.genero}'

class Podcast(ElementoMultimedia):
    def __init__(self, titulo: str, duracion: int, fecha_lanzamiento: int, presentador: str, num_episodio: int, tema: str)-> None:
        super().__init__(titulo, duracion, fecha_lanzamiento)

        if num_episodio < 1:
            raise ValueError('El número de episodio debe ser al menos 1')
        
        self.presentador = presentador
        self.num_episodio = num_episodio
        self.tema = tema

    def mostrar(self) -> str:
        mostrar_elemento = super().mostrar()
        return f'{mostrar_elemento} episodio {self.num_episodio} sobre {self.tema} del presentador {self.presentador}'
