from Biblioteca import Biblioteca
import pickle
import os

class Main:
    
    ARCHIVO_BIBLIOTECA= 'biblioteca.pkl'
    
    def cargar_biblioteca():
        
        """Carga la biblioteca desde un archivo, o crea uno nuevo si no existe."""
        
        if os.path.exists(Main.ARCHIVO_BIBLIOTECA):
            # Si el archivo existe, cargarlo
            with open(Main.ARCHIVO_BIBLIOTECA, 'rb') as archivo:
                biblioteca = pickle.load(archivo)
                print("Biblioteca cargada exitosamente. ")
                return biblioteca
        else:
            # Si no existe, se inicializa una biblioteca vacía y se guarda el archivo
            biblioteca = Biblioteca("Babel","Puerto Valdivia")
            print("Biblioteca creada exitosamente.")
            Main.guardar_biblioteca(biblioteca)
        
    def guardar_biblioteca(biblioteca):
        
        """Guarda la biblioteca en un archivo"""
        
        with open(Main.ARCHIVO_BIBLIOTECA, 'wb') as archivo:
            pickle.dump(biblioteca, archivo)
            print("Biblioteca guardada exitosamente.")
            
    def run():
        
        biblioteca = Main.cargar_biblioteca()
        
        if biblioteca is not None:
            biblioteca.agregar_estante("Ciencias Sociales")
            biblioteca.agregar_estante("Ciencias Exactas")
            biblioteca.agregar_estante("Ciencias Humanas")
            biblioteca.agregar_estante("Ciencias Políticas")
            biblioteca.agregar_estante("Literatura")
        else:
            print("No se pudo cargar la biblioteca. Inténtelo nuevamente.")
        
        while True:
            Main.mostrar_menu_principal()
            opcion = int(input("¿Qué desea hacer? (1-9): "))
            if opcion == 1:
                Main.gestionar_biblioteca(biblioteca)
            elif opcion == 2:
                Main.gestionar_libros(biblioteca)
            elif opcion == 3:
                Main.gestionar_lectores(biblioteca)
            elif opcion == 4:
                Main.gestionar_bibliotecarios(biblioteca)
            elif opcion == 5:
                Main.gestionar_autores(biblioteca)
            elif opcion == 6:
                Main.gestionar_prestamos(biblioteca)
            elif opcion == 7:
                Main.guardar_y_salir(biblioteca)
                break
            else:
                print("Opción inválida.")
            
    def mostrar_menu_principal():
        print("""\n--------MENÚ PRINCIPAL--------\n
    1. Gestionar Biblioteca.
    2. Gestionar Libros.
    3. Gestionar Lectores.
    4. Gestionar Bibliotecarios.
    5. Gestionar Autores.
    6. Gestionar Préstamos.
    7. Guardar y Salir\n
    """)

    def mostrar_menu_biblioteca():
        print("""\n--------MENÚ BIBLIOTECA--------\n
1. Buscar Multa.
2. Buscar Recibo.
3. Mostrar Libros Registrados.
4. Mostrar Lectores Registrados.
5. Mostrar Bibliotecarios Registrados.
6. Mostrar Autores Registrados.
7. Volver al Menú Principal.
8. Guardar y Salir\n""")
    
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
    9. Guardar y Salir. \n
    """)

    def mostrar_menu_lectores():
        print("""\n---------MENÚ LECTORES---------\n
    1. Agregar Lector.
    2. Eliminar Lector.
    3. Buscar Lector.
    4. Volver al Menú Principal.
    5. Guardar y Salir.\n
    """)

    def mostrar_menu_bibliotecarios():
        print("""\n---------MENÚ BIBLIOTECARIOS---------\n
    1. Agregar Bibliotecario.
    2. Eliminar Bibliotecario.
    3. Buscar Bibliotecario.
    4. Volver al Menú Principal.
    5. Guardar y Salir.\n
    """)

    def mostrar_menu_autores():
        print("""\n---------MENÚ AUTORES---------\n
    1. Agregar Autor.
    2. Eliminar Autor.
    3. Buscar Autor.
    4. Volver al Menú Principal.
    5. Guardar y Salir.\n
    """)

    def mostrar_menu_prestamos():
        print("""\n---------MENÚ PRÉSTAMOS---------\n
1. Buscar Préstamo.
2. Consultar Multa Asociada Préstamo.
3. Volver al Menú Principal.
4. Guardar y Salir. """)
        
    def mostrar_opciones_listar_libros(biblioteca):
        print("""
1. Listar Libros por Estado.
2. Listar Libros por Autor.
3. Listar Libros por Área del Conocimiento.
4. Listar Libros por Género.
5. Listar Libros por Fecha de Publicación.
""")
    
    def gestionar_biblioteca(biblioteca):
        
        while True:
            
            Main.mostrar_menu_biblioteca()
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1:
                Main.buscar_multa()
                
            elif opcion == 2:
                Main.buscar_recibo()
            
            elif opcion == 3: # Mostrar libros registrados
                
                libros = biblioteca.get_libros() # Retorna una ndarray
                
                if libros.size >= 1:
                    print("\nLos Libros registrados son:\n")
                    for i in range(len(libros)):
                        if libros[i] is not None:
                            print(libros[i])
                        
            elif opcion == 7:
                break
            elif opcion == 8:
                Main.guardar_y_salir(biblioteca)
                break
                
    def gestionar_libros(biblioteca):
        
        while True:
            
            Main.mostrar_menu_libros()
            opcion = int(input("Ingrese una opción (1-9): "))
            
            if opcion == 1: # Agregar Libro
                
                titulo = input("Ingrese el titulo: ")
                codigo_isbn = input("Ingrese el codigo ISBN: ")
                autor = input("Ingrese el primer nombre y primer apellido del autor separados por un espacio: ")
                area_del_conocimiento = input("Ingrese el área del conocimiento: ")
                genero = input("Ingrese el género: ")
                nro_paginas = input("Ingrese el número de páginas: ")
                fecha_publicacion = input("Ingrese el año de publicación: ")
                origen = input("Ingrese el origen del libro: ")
                
                biblioteca.agregar_libro(titulo,codigo_isbn,autor,area_del_conocimiento,genero,nro_paginas,fecha_publicacion,origen)
                
            elif opcion == 2: # Eliminar Libro
                
                titulo = input("Ingrese el titulo: ")
                codigo_isbn = input("Ingrese el codigo ISBN: ")
                
                biblioteca.eliminar_libro(titulo, codigo_isbn)
                
            elif opcion == 3: # Prestar libro
                
                titulo = input("Ingrese el titulo: ")
                codigo_isbn = input("Ingrese el codigo ISBN: ")
                identificacion_lector = input("Ingrese la identificación del lector: ")
                fecha_prestamo = input("Ingrese la fecha de prestamo en el formato DD/MM/Y: ")
                
                biblioteca.prestar_libro(titulo, codigo_isbn, identificacion_lector, fecha_prestamo)
                
            elif opcion == 4: # Renovar Prestamo Libro
                
                identificacion_lector = input("Ingrese la identificación del lector: ")
                codigo_prestamo = input("Ingrese el código del préstamo: ")
                
                biblioteca.renovar_prestamo(codigo_prestamo, identificacion_lector)
                
            elif opcion == 5: # Devolver Libro
                
                codigo_prestamo = input("Ingrese el código del préstamo del libro a devolver: ")
                identificacion_lector = input("Ingrese la identificación del lector: ")
                fecha_entrega = input("Ingrese la fecha de entrega en el formato DD/MM/Y: ")
                
                biblioteca.recibir_libro_devuelto(codigo_prestamo, identificacion_lector, fecha_entrega)
                
            elif opcion == 6: # Buscar libro
                
                titulo = input("Ingres el titulo: ")
                codigo_isbn = input("Ingrese el código ISBN: ")
                
                biblioteca.buscar_libro(titulo, codigo_isbn)
                
            elif opcion == 7: # Listar
                Main.mostrar_opciones_listar_libros()
                opcion_listar = int(input("Ingrese la opción para listar: "))
                
                if opcion_listar == 1: # Listar por Estado
                    estado = input("Ingrese el estado del libro con el que desea listar: ")
                    biblioteca.listar_por_estado(estado)
                
                elif opcion_listar == 2: # Listar por Autor
                    
                    nombre = input("Ingrese el nombre del autor: ")
                    apellido = input("Ingrese el apellido del autor: ")
                    biblioteca.listar_por_autor(nombre, apellido)
                
                elif opcion_listar == 3: # Listar por area del conocimiento
                    area_del_conocimiento = input("Ingrese el área del conocimiento: ")
                    biblioteca.listar_por_area_del_conocimiento(area_del_conocimiento)
                
                elif opcion_listar == 4: # Listar por genero
                    genero = input("Ingrese el género: ")
                    biblioteca.listar_por_genero(genero)
                
                elif opcion_listar == 5: # Listar por año de publicacion
                    anio_publicacion = input("Ingrese el año de publicación: ")
                    biblioteca.listar_por_anio_publicacion(anio_publicacion)
                    
                else:
                    print("Opción inválida.")
                
            elif opcion == 8:
                break
            elif opcion == 9:
                Main.guardar_y_salir(biblioteca)
                break
            else:
                print("Opción no válida.")

    def gestionar_lectores(biblioteca):
        
        while True:
            
            Main.mostrar_menu_lectores()
            opcion = int(input("Ingrese una opción (1-5): "))
            
            if opcion == 1: # Agregar Lector
                
                nombre = input("Ingrese el nombre del lector: ")
                apellido = input("Ingrese el apellido del lector: ")
                identificacion = input("Ingrese la identificación del lector: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del lector en el formato DD/MM/Y: ")
                email = input("Ingrese el correo electrónico del lector: ")
                
                biblioteca.agregar_lector(nombre, apellido, fecha_nacimiento, identificacion, email)
                
            elif opcion == 2: # Eliminar Lector
                
                identificacion= input("Ingrese la identificación del lector: ")
                biblioteca.eliminar_lector(identificacion)

            elif opcion == 3: # Buscar Lector
                
                identificacion = input("Ingrese la identificación del lector: ")
                biblioteca.buscar_lector(identificacion)

            elif opcion == 4: # Volver al menú principal
                break
            elif opcion == 5: # Guardar y salir
                Main.guardar_y_salir(biblioteca)
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")    

    def gestionar_bibliotecarios(biblioteca):
        
        while True:
            
            Main.mostrar_menu_bibliotecarios()
            opcion = int(input("Ingrese una opción (1-5): "))
            
            if opcion == 1: # Agregar Bibliotecario
                
                nombre= input("Ingrese el nombre del bibliotecario: ")
                apellido=input("Ingrese el apellido del bibliotecario: ")
                fecha_nacimiento=input("Ingrese la fecha de nacimiento del bibliotecario (DD/MM/Y)")
                identificacion= input("Ingrese la identificación del bibliotecario: ")
                email= input("Ingrese el email del bibliotecario: ")  
                
                biblioteca.agregar_bibliotecario(nombre, apellido, fecha_nacimiento, identificacion, email)
                
            elif opcion == 2: # Eliminar Bibliotecario
                
                identificacion= input("Ingrese la identificación del bibliotecario: ")
                biblioteca.eliminar_bibliotecario(identificacion)

            elif opcion == 3: # Buscar Bibliotecario
                
                identificacion= input("Ingrese la identificación del bibliotecario: ")
                biblioteca.buscar_bibliotecario(identificacion)
                
            elif opcion == 4: # Volver al menú principal
                break
            elif opcion == 5: # Guardar y salir
                Main.guardar_y_salir(biblioteca)
                break
            else:
                print("Opción no válida.")

    def gestionar_autores(biblioteca):
        
        while True:
            
            Main.mostrar_menu_autores()
            opcion = int(input("Ingrese una opción (1-5): "))
            
            if opcion == 1: # Agregar Autor
                
                nombre = input("Ingrese el nombre del autor: ")
                apellido = input("Ingrese el apellido del autor: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del autor (DD/MM/Y): ")
                fecha_fallecimiento = input("Ingrese la fecha de fallecimiento del autor (DD/MM/Y): ")
                pais_origen = input("Ingrese el pais de origen del autor: ")
                biblioteca.agregar_autor(nombre,apellido,fecha_nacimiento,fecha_fallecimiento,pais_origen)
                
            elif opcion == 2: # Eliminar autor
                
                nombre= input("Ingrese el nombre del autor: ")
                apellido=input("Ingrese el apellido del autor: ")
                
                biblioteca.eliminar_autor(nombre,apellido)
    
            elif opcion == 3: # Buscar autor
                
                nombre= input("Ingrese el nombre del autor: ")
                apellido=input("Ingrese el apellido del autor: ")
                
                biblioteca.buscar_autor(nombre,apellido)
                
            elif opcion == 4: # Volver al menu principal
                break
            elif opcion == 5: # Guardar y salir
                Main.guardar_y_salir(biblioteca)
                break
            else:
                print("Opción no válida.")

    def gestionar_prestamos(biblioteca):
        
        while True:
            
            Main.mostrar_menu_prestamos()
            opcion = int(input("Ingrese una opción (1-2) : "))
            
            if opcion == 1: # Buscar prestamo
                
                codigo_prestamo = input("ingrese el codigo del prestamo: ")
                prestamo = biblioteca.buscar_prestamo(codigo_prestamo)
                
                if prestamo is not None:
                    print(f"Prestamo encontrado: {prestamo}")
                else:
                    print(f"Prestamo {codigo_prestamo} no encontrado.")

            elif opcion == 2: # Consultar multa
                
                codigo_prestamo = input("ingrese el codigo del prestamo:")
                prestamo = biblioteca.buscar_prestamo(codigo_prestamo)
                multa = prestamo.get_multa()
                
                if prestamo is not None:
                    if multa is not None:
                        print(f"Información de la Multa del Préstamo {codigo_prestamo}: {multa}")
                    else:
                        print(f"El Préstamo {codigo_prestamo} no tiene una multa asociada. ")
                else:
                    print(f"No se pudo comprobar la existencia de una Multa. Prestamo {codigo_prestamo} no encontrado.")

            elif opcion == 3: # Volver al menu principal
                break
            
            elif opcion == 4: # Guardar y salir
                Main.guardar_y_salir(biblioteca)
                break
            
            else:
                print("Opción no válida.")        

    def buscar_multa(biblioteca):
        
        while True: 
                
            codigo_multa = input("Ingrese el código de la multa: ")
            multa = biblioteca.buscar_multa(codigo_multa)
            
            if multa is not None:
                print(multa)
            else:
                print(f"La multa {codigo_multa} no existe. ")
                
            break
                
    def buscar_recibo(biblioteca):
        
        while True:
            
            codigo_recibo = input("Ingrese el código del recibo: ")
            recibo = biblioteca.buscar_recibo(codigo_recibo)
            
            if recibo is not None:
                print(recibo)
            else:
                print(f"Recibo {codigo_recibo} no encontrado.")
                
            break
    
    def guardar_y_salir(biblioteca):
        Main.guardar_biblioteca(biblioteca)
        print("Biblioteca guardada exitosamente.")
        
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