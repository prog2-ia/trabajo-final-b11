# Traemos las clases desde tus otros archivos
from tipos_audio import Cancion, Podcast
from biblioteca import Biblioteca
from perfiles import Usuario, Artista
from album import Album


def mostrar_menu():
    print('\n' + '=' * 40)
    print('Mi plataforma de Música ')
    print('=' * 40)
    print('1. Ver catálogo completo')
    print('2. Añadir una canción nueva')
    print('3. Ver mi perfil de usuario')
    print('4. Salir')
    print('-' * 40)

if __name__ == '__main__':
    mi_biblioteca = Biblioteca('Catálogo Principal')
    usuario_actual = Usuario('Pedro', 'picapiedra@gmail.com')

    artista_prueba = Artista('Bad Bunny', 'Reggaetón')
    cancion1 = Cancion('Tití Me Preguntó', 4.03, '2022', artista_prueba.nombre, 'Un Verano Sin Ti', 'Reggaetón')
    cancion2 = Cancion('Safaera', 4.55, '2020', artista_prueba.nombre, 'YHLQMDLG', 'Reggaetón')

    mi_biblioteca.agregar_al_catalogo(cancion1)
    mi_biblioteca.agregar_al_catalogo(cancion2)

    # Menú interactivo
    while True:
        mostrar_menu()
        opcion = input('Elige una opción (1-4): ')

        if opcion == '1':
            print('Catálogo actual: ')
            print(mi_biblioteca.mostrar_catalogo())

        elif opcion == '2':
            print('Añadir nueva canción: ')
            titulo = input('Dime el título: ')

            duracion = float(input('Dime la duración (ej. 3.5): '))

            fecha = input('Dime el año de lanzamiento: ')
            artista = input('Dime el nombre del artista: ')
            album = input('Dime el nombre del álbum: ')
            genero = input('Dime el género musical: ')

            # Creamos la canción con nuestras clases y la guardamos
            nueva_cancion = Cancion(titulo, duracion, fecha, artista, album, genero)
            mensaje = mi_biblioteca.agregar_al_catalogo(nueva_cancion)
            print(f' Hecho. {mensaje}')

        elif opcion == '3':
            print('Perfil de usuario: ')
            print(usuario_actual.mostrar_perfil())

        elif opcion == '4':
            print('¡Gracias por usar la plataforma!')
            break

        else:
            print('Opción no válida. Escribe un número del 1 al 4.')

