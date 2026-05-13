from abc import ABC, abstractmethod
from typing import Any

class ElementoMultimedia(ABC):
    def __init__(self,titulo: str,duracion: int,fecha_lanzamiento: int) -> None:
        self.titulo = titulo
        self.duracion = duracion
        self.fecha_lanzamiento = fecha_lanzamiento

        #Impedimos que la fecha de lanzamiento sea negativa
        if fecha_lanzamiento < 0:
            raise ValueError('La fecha de lanzamiento no puede ser negaiva')

    @property
    def duracion(self) -> int | float:
        return self._duracion

    # Si duracion es menor de 0, se asocia un valor predeterminado 3.0.
    @duracion.setter
    def duracion(self, valor: int | float) -> None:
        # Manejamos un posible error de tipo de dato
        if not isinstance(valor, int | float):
            raise TypeError('El tipo de dato debe ser "int" o "float"')
        if valor <= 0:
            self._duracion = 3.0
        else:
            self._duracion = valor

    # Metodo abstracto para utilizarlo en otras clases con diferentes contenidos
    @abstractmethod
    def mostrar(self) -> str:
        return f'Estas reproduciendo {self.titulo} lanzada el {self.fecha_lanzamiento} y de duracion {self.duracion}'

    # Compara si dos pistas son iguales
    def __eq__(self, otro: Any) -> bool:
        if isinstance(otro, ElementoMultimedia):
            return self.titulo == otro.titulo and self.duracion == otro.duracion
        return False

