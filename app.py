from dao.libro_dao import LibroDAO
from models.libro import Libro

from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

import flet as ft
from ui.main_window import main_window


def ver_libros():
    try:
            
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todos()

        print("===Libros en la biblioteca===")
        if len(libros) ==0:
            print("No hay libros")
        else:
            for libro in libros:
                print(
                    f"ID: {libro.id},"
                    f"Titulo:{libro.titulo},"
                    f"Autor: {libro.autor}, ISBM: {libro.isbn},"
                    f"Disponible: {'Si' if libro.disponible else 'No'}"
                )
                print("--------------------------")
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def insertar_libro():
    titulo= input("Escribe el titulo del nuevo libro: ")
    autor = int(input("Escribe el id del autor: "))
    isbn = input("Ingrese el isbn del nuevo libro: ")
    disponible = True
    try: 
        libro_dao=LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(id,titulo,autor,isbn,disponible)
        libro_dao.insertar(libro)
        print("Insercion realizada con exito")
    except Exception as e:
        print("Error al insertar un nuevo libro")
        print(e)
def actualizar_libro():
    print("Selecciona el libro a actualizar: ")
    try:
        libro_dao= LibroDAO()
        ver_libros()
        id= int(input("Escribe el id del libro a actualizar: "))
        titulo = input("Escribo el nuevo titulo: ")
        autor = input("Escribe el nuevo autor")
        isbn = input("Escribe el nuevo ISBN")
        disponible = bool(input("Escribe el nuevo valor de disponible"))
        libro = Libro(id,titulo,autor,isbn,disponible)
        libro_dao.actualizar(libro)
        print(f"El ibro {id} se ha actualizado exitosamente")
    except Exception as e:
        print(f"Error al actualizar un libro{id}")
        print(e)

def eliminar_libro():
        try:
            libro_dao = LibroDAO()
            print("Lista de libros disponibles: ")
            ver_libros()
            id = int(input("Escribe el id del libro a eliminar: "))
            libro_dao.eliminar(id)
            print(f"El libro {id} ha sido eliminado con exito")
        except Exception as e:
            print("Error al eliminar el libro{id}")
            print(e)


def menu_libros():
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro")
    print("3. Actualizar un libro disponible")
    print("4. Eliminar un libro disponible")
    opcion = int(input("Selecciona una opcion de 1-4: "))

    match opcion:
        case 1: 
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4:
            eliminar_libro()

def menu_usuarios():
    print("1. Ver todos los usuarios")
    print("2. Insertar un nuevo usuarios")
    print("3. Actualizar un usuario existente")
    print("4. Eliminar un usuario")
    opcion = int(input("Selecciona una opcion de 1-4: "))

    match opcion:
        case 1: 
            ver_usuario()
        case 2:
            insertar_usuario()
        case 3:
            actualizar_usuario()
        case 4:
            eliminar_usuario()




def ver_usuario():
    try:
            
        usuario_dao = UsuarioDAO()
        usuarios = usuario_dao.obtener_todos()

        print("===Usuarios===")
        if len(usuarios) ==0:
            print("No hay usuarios")
        else:
            for usuario in usuarios:
                print(
                    f"ID: {usuario.id},"
                    f"Nombre: {usuario.nombre},"
                    f"Matricula: {usuario.matricula}"
                    f"Correo: {usuario.carrera},"
                    f"Carrera: {usuario.correo},"
                )
                print("--------------------------")
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def insertar_usuario():
    nombre= input("Escribe nombre del nuevo usuario: ")
    matricula = int(input("ingrese matricula del usuario: "))
    carrera = input("Ingrese carrera del usuario: ")
    correo = input("Escribe la direccion de correo: ")
    
    try: 
        usuario_dao=UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1
        usuario = Usuario(id, nombre, matricula, carrera, correo)
        usuario_dao.insertar(usuario)
        print("Insercion realizada con exito")
    except Exception as e:
        print("Error al insertar un nuevo usuario")
        print(e)

def actualizar_usuario():
    print("Selecciona el usuario a actualizar: ")
    try:
        usuario_dao= UsuarioDAO()
        ver_usuario()
        id= int(input("Escribe el id del usuario a actualizar: "))
        nombre = input("Escribo el nuevo nombre: ")
        matricula = input("Escribe nueva matricula: ")
        carrera = input("Escribe la carrera: ")
        correo = input("Escribe el nuevo correo: ")
        usuario = Usuario(id,nombre,matricula,carrera,correo)
        usuario_dao.actualizar(usuario)
        print(f"El usuario {id} se ha actualizado exitosamente")
    except Exception as e:
        print(f"Error al actualizar un usuario{id}")
        print(e)

def eliminar_usuario():
        try:
            usuario_dao = UsuarioDAO()
            print("Lista de usuarios disponibles: ")
            ver_usuario()
            id = int(input("Escribe el id del usuario a eliminar: "))
            usuario_dao.eliminar(id)
            print(f"El usuario {id} ha sido eliminado con exito")
        except Exception as e:
            print("Error al eliminar el usuario {id}")
            print(e)


# def main():
#     print("=========BIBLIOTECA UNIVERSITARIA=========")
#     print("Menu de opciones")
#     print("1. libros")
#     print("2. Usuario")

#     opc = int(input("Selecciona una opcion: "))

#     match opc:
#         case 1:
#             menu_libros()
#         case 2:
#             menu_usuarios()



# if __name__ == "__main__":
#     main()

ft.app(target=main_window)
