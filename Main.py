
from Biblioteca import Biblioteca
import datetime

class Main:
    
    @staticmethod
    def run():
        
        biblioteca = Biblioteca("Babel","Puerto Valdivia")
        
        biblioteca.agregar_estante("Ciencias Sociales")
        biblioteca.agregar_estante("Ciencias Exactas")
        biblioteca.agregar_estante("Ciencias Humanas")
        biblioteca.agregar_estante("Ciencias Políticas")
        biblioteca.agregar_estante("Literatura")
        
        while True:
            Main.mostrar_menu_principal()
            opcion = input("¿Qué desea hacer? (1-7): ")
            if opcion == "1":
                Main.gestionar_libros(biblioteca)
            elif opcion == "2":
                Main.gestionar_lectores(biblioteca)
            elif opcion == "3":
                Main.gestionar_rios(biblioteca)
            elif opcion == "4":
                Main.gestionar_autores(biblioteca)
            elif opcion == "5":
                Main.gestionar_prestamos(biblioteca)
            elif opcion == "6":
                Main.gestionar_multas(biblioteca)
            elif opcion == "7":
                Main.gestionar_recibos(biblioteca)
            elif opcion == "8":
                Main.guardar_y_salir(biblioteca)
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción entre 1 y 8.")
            
    def mostrar_menu_principal():
        print("""\n--------MENÚ PRINCIPAL--------\n
    1. Gestión de Libros.
    2. Gestión de Lectores.
    3. Gestión de Bibliotecarios.
    4. Gestión de Autores.
    5. Gestión de Préstamos.
    6. Gestión de Multas.
    7. Gestión de Recibos.
    8. Salir\n
    """)

    def mostrar_menu_libros():
        print("""\n---------MENÚ LIBROS---------\n
    1. Agregar Libro.
    2. Eliminar Libro.
    3. Prestar Libro.
    4. Renovar Préstamo.
    5. Devolver Libro.
    6. Buscar Libro.
    7. Listar Libros.
    8. Volver al Menú Principal.
    9. Salir. \n
    """)

    def mostrar_menu_lectores():
        print("""\n---------MENÚ LECTORES---------\n
    1. Agregar Lector.
    2. Eliminar Lector.
    3. Buscar Lector.
    4. Volver al Menú Principal.
    5. Salir.\n
    """)

    def mostrar_menu_bibliotecarios():
        print("""\n---------MENÚ BIBLIOTECARIOS---------\n
    1. Agregar Bibliotecario.
    2. Eliminar Bibliotecario.
    3. Buscar Bibliotecario.
    4. Volver al Menú Principal.
    5. Salir.\n
    """)

    def mostrar_menu_autores():
        print("""\n---------MENÚ AUTORES---------\n
    1. Agregar Autor.
    2. Eliminar Autor.
    3. Buscar Autor.
    4. Volver al Menú Principal.
    5. Salir.\n
    """)

    def mostrar_menu_prestamos():
        print("""\n---------MENÚ PRÉSTAMOS---------\n
    1. Buscar Préstamo.
    2. Consular Fecha Préstamo.
    3. Consultar Fecha Devolución.
    4. Consultar Estado.
    5. Consular Multa.
    6. Volver al Menú Principal.
    7. Salir.\n
    """)

    def mostrar_menu_multas():
        print("""\n---------MENÚ MULTAS---------\n
    1. Buscar Multa.
    2. Consultar Fecha Inicio.
    3. Consultar Fecha Fin.
    4. Consultar Días Penalización.
    5. Consultar Estado.
    6. Volver al Menú Principal.
    7. Salir.\n
    """)

    def mostrar_menu_recibos():
        print("""\n---------MENÚ RECIBOS---------\n
    1. Buscar Recibo.
    2. Consultar Fecha Emisión.
    3. Consultar Información.
    4. Volver al Menú Principal.
    5. Salir.\n
    """)

    def gestionar_libros(biblioteca=Biblioteca):
        while True:
            Main.mostrar_menu_libros()
            opcion = int(input("Ingrese una opción (1-9): "))
            if opcion == 1: # Agregar Libro
                titulo = input("Ingrese el titulo del libro.")
                codigo_isbn = input("Ingrese el codigo ISBN del libro.")
                autor = input("Ingrese el primer nombre y primer apellido del autor del libro separados por un espacio.")
                area_del_conocimiento = input("Ingrese el área del conocimiento del libro.")
                genero = input("Ingrese el género del libro.")
                nro_paginas = input("Ingrese el número de páginas del libro.")
                fecha_publicacion = input("Ingrese la fecha de publicación del libro en el formato DD/MM/Y")
                origen = input("Ingrese el origen del libro.")
                biblioteca.agregar_libro(titulo,codigo_isbn,autor,area_del_conocimiento,genero,nro_paginas,fecha_publicacion,origen)
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                pass
            elif opcion == 7:
                pass
            elif opcion == 8:
                break
            elif opcion == 9:
                Main.guardar_y_salir()
            else:
                print("Opción no válida. Por favor, una opción entre 1 y 9.")

    def gestionar_lectores(biblioteca=Biblioteca):
        while True:
            Main.mostrar_menu_lectores()
            opcion = int(input("Ingrese una opción (1-5): "))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                break
            elif opcion == 5:
                Main.guardar_y_salir()
            else:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")    

    def gestionar_bibliotecarios(biblioteca=Biblioteca):
        while True:
            Main.mostrar_menu_bibliotecarios()
            opcion = int(input("Ingrese una opción (1-5): "))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                break
            elif opcion == 5:
                Main.guardar_y_salir()
            else:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")

    def gestionar_autores(biblioteca=Biblioteca):
        while True:
            Main.mostrar_menu_autores()
            opcion = int(input("Ingrese una opción (1-5): "))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                break
            elif opcion == 5:
                Main.guardar_y_salir()
            else:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")

    def gestionar_prestamos(biblioteca=Biblioteca):
        while True:
            Main.mostrar_menu_prestamos()
            opcion = int(input("Ingrese una opción (1-7): "))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                break
            elif opcion == 7:
                Main.guardar_y_salir()
            else:
                print("Opción no válida. Por favor, una opción entre 1 y 7.")        

    def gestionar_multas(biblioteca=Biblioteca):
        while True:
            Main.mostrar_menu_multas()
            opcion = int(input("Ingrese una opción (1-7): "))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                break
            elif opcion == 7:
                Main.guardar_y_salir()
            else:
                print("Opción no válida. Por favor, una opción entre 1 y 7.")

    def gestionar_recibos(biblioteca=Biblioteca):
        while True:
            Main.mostrar_menu_recibos()
            opcion = int(input("Ingrese una opción (1-7): "))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                break
            elif opcion == 7:
                Main.guardar_y_salir()
            else:
                print("Opción no válida. Por favor, una opción entre 1 y 7.")
            
    def guardar_y_salir(biblioteca=Biblioteca):
        pass
Main.run()


"""
class Prueba:
    def run():
        
        biblioteca = Biblioteca("Babel","Puerto Valdivia")
        
        # estantes
        
        biblioteca.agregar_estante("Ciencias Sociales")
        biblioteca.agregar_estante("Ciencias Exactas")
        biblioteca.agregar_estante("Ciencias Humanas")
        biblioteca.agregar_estante("Ciencias Políticas")
        biblioteca.agregar_estante("Literatura")
        
        #print(biblioteca.get_estantes())
        
        biblioteca.agregar_bibliotecario("Uberney","Perez",datetime.date(1982,6,7),"32534634","uber@gmail.com")
        print(biblioteca.get_bibliotecarios())
        
        # lectores
        
        biblioteca.agregar_lector("Nicole","Adarve", datetime.date(2006,9,9),"12324234","nico@gmail.com")
        biblioteca.agregar_lector("Karen","Vergara", datetime.date(2007,6,3),"2345","karen@gmail.com")
        biblioteca.agregar_lector("Pepe","Martinez", datetime.date(1999,9,9),"3453235","pepemartinez@gmail.com")
        print(biblioteca.get_lectores())
        
        # autores
        
        biblioteca.agregar_autor("Gabo","Gabito","12/9/1984","3/2/2000","Colombia")
        biblioteca.agregar_autor("Lechuza","Perez",datetime.date(1777,7,7),datetime.date(2000,2,2),"Venezuela")
        biblioteca.agregar_autor("Laura","Esquiveq",datetime.date(1998,8,9),datetime.date(2023,12,8),"Canadá")
        print(biblioteca.get_autores())
        
        # agregar libros
                
        biblioteca.agregar_libro("Cien años","01","Gabo Gabito","Literatura","Novela",14,datetime.date(2000,4,5),"Donacion")
        biblioteca.agregar_libro("Cien lagrimas","02","Lechuza Perez","Ciencias Sociales","Enciclopedia",200,datetime.date(2004,9,6),"Donacion")
        biblioteca.agregar_libro("Chocolate con cafe","234","Laura Esquiveq","Ciencias Exactas","Diccionario",444,datetime.date(1888,8,8),"Adquirido por la Biblioteca")    
        
        # prestar libros
        
        biblioteca.prestar_libro("Cien años","01","12324234","13/11/2024")
        biblioteca.prestar_libro("Cien lagrimas","02","2345","14/11/2024")
        biblioteca.prestar_libro("Chocolate con cafe","234","3453235","15/11/2024")
        print(biblioteca.get_libros_prestados())
        
        # renovar prestamo de libros
        
        biblioteca.renovar_prestamo("P1","12324234")
        
        # recibir libros devueltos

        biblioteca.recibir_libro_devuelto("P1","12324234","15/11/2024")
        biblioteca.recibir_libro_devuelto("P2","2345","01/01/2025")
        biblioteca.recibir_libro_devuelto("P3","3453235","18/12/2024")
        
        # listar 
        
        print(biblioteca.listar_por_autor("Lechuza","Perez"))
        print(biblioteca.listar_por_autor("Gabo","Gabito"))
        print(biblioteca.listar_por_estado("Disponible"))
        print(biblioteca.listar_por_estado("Prestado"))
        print(biblioteca.listar_por_area_del_conocimiento("Ciencias Sociales"))
        print(biblioteca.listar_por_genero("Novela"))
        print(biblioteca.listar_por_fecha_publicacion(datetime.date(1888,8,8)))

#Prueba.run()
"""