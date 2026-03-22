from abc import ABC, abstractmethod

class ElementoMultimedia(ABC):
    def __init__(self,titulo:str,duracion,fecha_lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.fecha_lanzamiento = fecha_lanzamiento

    @property
    def duracion(self):
        return self._duracion

    # Si duracion es menor de 0, se asocia un valor predeterminado 3.0.
    @duracion.setter
    def duracion(self, valor):
        if valor <= 0:
            self._duracion = 3.0
        else:
            self._duracion = valor

    # Metodo abstracto para utilizarlo en otras clases con diferentes contenidos
    @abstractmethod
    def mostrar(self):
        return f'Estas reproduciendo {self.titulo} lanzada el {self.fecha_lanzamiento} y de duracion {self.duracion}'

    # Compara si dos pistas son iguales
    def __eq__(self, otro):
        if isinstance(otro, ElementoMultimedia):
            return self.titulo == otro.titulo and self.duracion == otro.duracion
        else:
            return False

