class Usuario:
    def __init__(self, nombre, gmail):
        self.nombre = nombre
        self.gmail = gmail
    def mostrar_perfil(self):
        return f'Perfil de Usuario | Nombre: {self.nombre} | Correo: {self.gmail}'

class Artista:
    def __init__(self, nombre, genero_principal):
        self.nombre = nombre
        self.genero_principal = genero_principal
        self.oyentes_mensuales= 0
    def actualizar_oyentes(self,cantidad):
        self.oyentes_mensuales = cantidad
    def mostrar_perfil(self):
        return f' Artista: {self.nombre} | Género: {self.genero_principal} | Oyentes: {self.oyentes_mensuales}'