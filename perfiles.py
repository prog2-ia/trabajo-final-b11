class Usuario:
    def __init__(self, nombre: str, gmail: str) -> None:
        self.nombre = nombre
        self.gmail = gmail
    def mostrar_perfil(self) -> str:
        return f'Perfil de Usuario | Nombre: {self.nombre} | Correo: {self.gmail}'

class Artista:
    def __init__(self, nombre: str, genero_principal: str) -> None:
        self.nombre = nombre
        self.genero_principal = genero_principal
        self.oyentes_mensuales = 0
    def actualizar_oyentes(self,cantidad: int) -> None:
        self.oyentes_mensuales = cantidad
    def mostrar_perfil(self) -> str:
        return f' Artista: {self.nombre} | Género: {self.genero_principal} | Oyentes: {self.oyentes_mensuales}'