from Biblioteca import Biblioteca
from Recibo import Recibo
import numpy as np
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
            biblioteca = Biblioteca("Babel")
            print("Biblioteca creada exitosamente.")
            Main.guardar_biblioteca(biblioteca)
        
    def guardar_biblioteca(biblioteca:Biblioteca):
        
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
            opcion = int(input("¿Qué desea hacer?: "))
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
                Main.guardar_y_salir(biblioteca)
                break
            else:
                print(f"Opción {opcion} inválida. Por favor, intente nuevamente.")
            
    def mostrar_menu_principal():
        print("""\n--------MENÚ PRINCIPAL--------\n
    1. Gestionar Biblioteca.
    2. Gestionar Libros.
    3. Gestionar Lectores.
    4. Gestionar Bibliotecarios.
    5. Gestionar Autores.
    6. Guardar y Salir\n
    """)

    def mostrar_menu_biblioteca():
        print("""\n--------MENÚ BIBLIOTECA--------\n
1. Buscar Multa.
2. Buscar Recibo.
3. Buscar Préstamo.
4. Consultar Multa Asociada a un Préstamo.
5. Listar Libros Registrados.
6. Listar Lectores Registrados.
7. Listar Bibliotecarios Registrados.
8. Listar Autores Registrados.
9. Listar Préstamos Realizados.
10. Listar Multas Generadas.
11. Listar Estantes Biblioteca.
12. Cambiar Nombre Bilioteca.
13. Volver al Menú Principal.""")
    
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
    """)

    def mostrar_menu_lectores():
        print("""\n---------MENÚ LECTORES---------\n
1. Agregar Lector.
2. Eliminar Lector.
3. Buscar Lector.
4. Listar Préstamos.
5. Listar Multas.
6. Listar Recibos.
7. Listar Préstamos Vigentes.
8. Consultar Número de Multas.
9. Consultar Número de Préstamos Vigentes.
10. Volver al Menú Principal.
    """)

    def mostrar_menu_bibliotecarios():
        print("""\n---------MENÚ BIBLIOTECARIOS---------\n
1. Agregar Bibliotecario.
2. Eliminar Bibliotecario.
3. Buscar Bibliotecario.
4. Volver al Menú Principal.
""")

    def mostrar_menu_autores():
        print("""\n---------MENÚ AUTORES---------\n
1. Agregar Autor.
2. Eliminar Autor.
3. Buscar Autor.
4. Volver al Menú Principal.
""")
        
    def mostrar_opciones_listar_libros():
        print("""\nLas opciones de listar son:\n
1. Listar Libros por Estado.
2. Listar Libros por Autor.
3. Listar Libros por Área del Conocimiento.
4. Listar Libros por Género.
5. Listar Libros por Fecha de Publicación.""")
    
    def gestionar_biblioteca(biblioteca:Biblioteca):
        
        while True:
            
            Main.mostrar_menu_biblioteca()
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1: # Buscar Multa
                
                codigo_multa = input("Ingrese el código de la multa: ")
                multa = biblioteca.buscar_multa(codigo_multa)
            
                if multa is not None:
                    print(multa)
                else:
                    print(f"La multa {codigo_multa} no existe. ")
                    
            elif opcion == 2: # Buscar recibo
                
                codigo_recibo = input("Ingrese el código del recibo: ")
                recibo = biblioteca.buscar_recibo(codigo_recibo)
                
                if recibo is not None:
                    print(recibo)
                else:
                    print(f"Recibo {codigo_recibo} no encontrado.")
            
            elif opcion == 3: # Buscar prestammo
                
                codigo_prestamo = input("Ingrese el código del Préstamo: ")
                prestamo = biblioteca.buscar_prestamo(codigo_prestamo)
                
                if prestamo is not None:
                    print(prestamo)
                else:
                    print(f"Préstamo {codigo_prestamo} no encontrado.")
            
            elif opcion == 4: # Consultar multa asociada a un prestamo
                
                codigo_prestamo = input("Ingrese el codigo del prestamo:")
                prestamo = biblioteca.buscar_prestamo(codigo_prestamo)
                
                if prestamo is not None:
                    multa = prestamo.get_multa()
                    if multa is not None:
                        print(f"""Información de la Multa del Préstamo {codigo_prestamo}:\n
{multa}""")
                    else:
                        print(f"El Préstamo {codigo_prestamo} no tiene una multa asociada. ")
                else:
                    print(f"No se pudo comprobar la existencia de una Multa. Prestamo {codigo_prestamo} no encontrado.")
                      
            elif opcion == 5: # Listar libros registrados
                
                libros = biblioteca.get_libros() # Retorna una ndarray
                
                if np.any(libros is not None): # Verifica si el ndarray tiene al menos un elemento no None
                    print("\nLos Libros registrados son:\n")
                    for i in range(biblioteca.get_nro_libros()):
                        if libros[i] is not None:
                            
                            titulo = libros[i].get_titulo()
                            codigo_isbn = libros[i].get_codigo_isbn()
                            autor = libros[i].get_autor()
                            area_del_conocimiento = libros[i].get_area_del_conocimiento()
                            
                            formato = f"< Titulo: '{titulo}' | ISBN: '{codigo_isbn}' | Autor: {autor} | Área: {area_del_conocimiento} >"
                            print(formato)
                else:
                    print("No hay libros registrados.")
            
            elif opcion == 6: # Listar lectores registrados
                
                lectores = biblioteca.get_lectores() # Retorna una lista
                
                lectores_validos = [lector for lector in lectores if lector is not None]
                
                if len(lectores_validos) > 0: # Verifica si la lista tiene al menos un elemento
                    print("\nLos lectores registrados son:\n")
                    for lector in lectores_validos:
                        
                        identificacion = lector.get_identificacion()
                        apellido = lector.get_apellido()
                        nombre = lector.get_nombre()
                        fecha_nacimiento = lector.get_fecha_nacimiento()
                        
                        formato = f"< Identificación: '{identificacion}' | Apellido: '{apellido}' | Nombre: '{nombre}' | Fecha de Nacimiento: '{fecha_nacimiento}' >"
                        
                        print(formato)
                else:
                    print("No hay lectores registrados.")
            
            elif opcion == 7: # Listar bibliotecarios registrados
                
                bibliotecarios = biblioteca.get_bibliotecarios()
                
                bibliotecarios_validos = [bibliotecario for bibliotecario in bibliotecarios if bibliotecario is not None]
                
                if len(bibliotecarios_validos) > 0:
                    print("\nLos bibliotecarios registrados son:\n")
                    for bibliotecario in bibliotecarios_validos:
                        
                        identificacion = bibliotecario.get_identificacion()
                        apellido = bibliotecario.get_apellido()
                        nombre = bibliotecario.get_nombre()
                        fecha_nacimiento = bibliotecario.get_fecha_nacimiento()
                        
                        formato = f"< Identificación: '{identificacion}' | Apellido: '{apellido}' | Nombre: '{nombre}' | Fecha de Nacimiento: '{fecha_nacimiento}' >"
                        
                        print(formato)
                        
                else:
                    print("No hay bibliotecarios registrados.")
                    
            elif opcion == 8: # Listar autores registrados
                
                autores = biblioteca.get_autores()
                
                autores_validos = [autor for autor in autores if autor is not None]
                
                if len(autores_validos) > 0:
                    print("\nLos autores registrados son:\n")
                    for autor in autores_validos:
                        
                        apellido = autor.get_apellido()
                        nombre = autor.get_nombre()
                        pais_origen = autor.get_pais_origen()
                        
                        formato = f"< Apellido: '{apellido}' | Nombre: '{nombre}' | Pais de Origen: '{pais_origen}' >"
                        
                        print(formato)
                        
                else:
                    print("No hay autores registrados.")
                
            elif opcion == 9: # Listar prestamos registrados
                
                prestamos = biblioteca.get_prestamos()
                
                prestamos_validos = [prestamo for prestamo in prestamos if prestamo is not None]
                
                if len(prestamos_validos):
                    print("\nLos Préstamos registrados son:\n")
                    for prestamo in prestamos_validos:
                        
                        codigo = prestamo.get_codigo()
                        identificacion_lector = prestamo.get_lector().get_identificacion()
                        titulo_libro = prestamo.get_libro().get_titulo()
                        codigo_isbn = prestamo.get_libro().get_codigo_isbn()
                        fecha_prestamo = prestamo.get_fecha_prestamo()
                        fecha_devolucion = prestamo.get_fecha_devolucion()
                        estado = prestamo.get_estado()
                        
                        formato = f"<Código: {codigo} | Lector: {identificacion_lector} | Libro: {titulo_libro}-{codigo_isbn} | Inicio: {fecha_prestamo} | Devolución: {fecha_devolucion} | Estado: {estado}>"
                        print(formato)
                else:
                    print("No hay Préstamos registrados.")
                    
            elif opcion == 10: # Listar multas generadas
                
                multas = biblioteca.get_multas()
                
                multas_validas = [multa for multa in multas if multa is not None]
                
                if len(multas_validas) > 0:
                    print("\nLas Multas generadas en la Biblioteca son: \n")
                    for multa in multas:
                        
                        codigo = multa.get_codigo()
                        codigo_prestamo = multa.get_prestamo().get_codigo()
                        identificacion_lector = multa.get_lector().get_identificacion()
                        fecha_inicio = multa.get_fecha_inicio()
                        fecha_fin = multa.get_fecha_fin()
                        dias_penalizacion = multa.get_dias_penalizacion()
                        estado = multa.get_estado()
                        
                        formato = f"< Código: {codigo} | Préstamo: {codigo_prestamo} | Lector: {identificacion_lector} | Inicio: {fecha_inicio} | Fin: {fecha_fin} | Penalización: {dias_penalizacion} dias. | Estado: {estado} >"
                        
                        print(formato)
                else:
                    print("No hay Multas registradas.")
                    
            elif opcion == 11: # Listar estantes
                
                estantes = biblioteca.get_estantes()
                
                if np.any(estantes is not None):
                    for estante in estantes:
                        if estante is not None:
                            print(estante)
                else:
                    print("La biblioteca no tiene estantes.")

            elif opcion == 12: # Cambiar nombre
                
                nombre_anterior = biblioteca.get_nombre()
                nuevo_nombre = input("Ingrese el nuevo nombre de la Biblioteca: ")
                biblioteca.set_nombre(nuevo_nombre)
                print(f"Nombre cambiado exitosamente. Nombre anterior: '{nombre_anterior}'. Nuevo Nombre: '{nuevo_nombre}'")
            
            elif opcion == 13: # Volver al menu principal
                break
            
            else:
                print(f"Opción '{opcion}' no válida.")
                
    def gestionar_libros(biblioteca:Biblioteca):
        
        while True:
            
            Main.mostrar_menu_libros()
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1: # Agregar Libro
                
                titulo = input("Ingrese el titulo: ")
                codigo_isbn = input("Ingrese el codigo ISBN: ")
                autor = input("Ingrese el primer nombre y primer apellido del autor separados por un espacio: ")
                area_del_conocimiento = input("Ingrese el área del conocimiento: ")
                genero = input("Ingrese el género: ")
                nro_paginas = input("Ingrese el número de páginas: ")
                fecha_publicacion = input("Ingrese el año de publicación: ")
                origen = input("Ingrese el origen del libro: ")
                
                print(biblioteca.agregar_libro(titulo,codigo_isbn,autor,area_del_conocimiento,genero,nro_paginas,fecha_publicacion,origen))
                
            elif opcion == 2: # Eliminar Libro
                
                titulo = input("Ingrese el titulo: ")
                codigo_isbn = input("Ingrese el codigo ISBN: ")
                
                if biblioteca.eliminar_libro(titulo, codigo_isbn) == True:
                    print(f"Libro '{titulo}' '{codigo_isbn}' eliminado exitosamente.")
                else:
                    print(f"No se pudo eliminar el libro. '{titulo}' '{codigo_isbn}' no está registrado.")
                
            elif opcion == 3: # Prestar libro
                
                titulo = input("Ingrese el titulo: ")
                codigo_isbn = input("Ingrese el codigo ISBN: ")
                identificacion_lector = input("Ingrese la identificación del lector: ")
                fecha_prestamo = input("Ingrese la fecha de prestamo en el formato DD/MM/Y: ")
                
                resultado = biblioteca.prestar_libro(titulo, codigo_isbn, identificacion_lector, fecha_prestamo)
                
                if isinstance(resultado, tuple):
                    prestamo, recibo = resultado
                    
                    print("Préstamo realizado con éxito.")
                    
                    visualizacion_prestamo = int(input("""¿Desea ver los detalles del Préstamo?
1. Si.
2. No.
                                          """))
                    
                    if visualizacion_prestamo == 1:
                        print("\nDetalles del Préstamo: \n")
                        print(prestamo)
                    
                    visualizacion_recibo = int(input("""¿Desea visualizar el recibo generado?
1. Si.
2. No.                                                     
                                                     """))
                    
                    if visualizacion_recibo == 1:
                        print("\nRecibo generado: \n")
                        print(recibo)
                else:
                    print(resultado)
                
            elif opcion == 4: # Renovar Prestamo Libro
                
                identificacion_lector = input("Ingrese la identificación del lector: ")
                codigo_prestamo = input("Ingrese el código del préstamo: ")
                
                resultado = biblioteca.renovar_prestamo(codigo_prestamo, identificacion_lector)
                
                if isinstance(resultado, Recibo):
                    print("Préstamo renovado exitosamente. ")
                    visualizacion_recibo = int(input("""¿Desea visualizar el recibo generado?
1. Si.
2. No.                                                     
                                                     """))
                    
                    if visualizacion_recibo == 1:
                        print(recibo)
                else:
                    print(resultado)
                
            elif opcion == 5: # Devolver Libro
                
                codigo_prestamo = input("Ingrese el código del préstamo del libro a devolver: ")
                identificacion_lector = input("Ingrese la identificación del lector: ")
                fecha_entrega = input("Ingrese la fecha de entrega en el formato DD/MM/Y: ")
                
                resultado = biblioteca.recibir_libro_devuelto(codigo_prestamo, identificacion_lector, fecha_entrega)
                
                if isinstance(resultado, Recibo):
                    print("Libro devuelto exitosamente.")
                    
                    visualizacion_recibo = int(input("""¿Desea ver el recibo generado?
1. Si.
2. No                                                     
                                                     """))
                    
                    if visualizacion_recibo == 1:
                        print(recibo)
                
                else:
                    print(resultado)
                    
            elif opcion == 6: # Buscar libro
                
                titulo = input("Ingres el titulo: ")
                codigo_isbn = input("Ingrese el código ISBN: ")
                
                _, libro = biblioteca.buscar_libro(titulo, codigo_isbn)
                
                if libro is not None:
                    print("Libro encontrado: ")
                    print(libro)
                else:
                    print(f"El libro '{titulo}' '{codigo_isbn}' no está registrado en la Biblioteca.")
                
            elif opcion == 7: # Listar
                Main.mostrar_opciones_listar_libros()
                opcion_listar = int(input("Ingrese la opción para listar: "))
                
                def listar(lista):
                    
                    for libro in lista:
                        
                        titulo = libro.get_titulo()
                        codigo_isbn = libro.get_codigo_isbn()
                        autor = libro.get_autor()
                        area = libro.get_area_del_conocimiento()
                        genero = libro.get_genero()
                        estado = libro.get_estado()
                        
                        formato = f"< Titulo: {titulo} | ISBN: {codigo_isbn} | Autor: {autor} | Área: {area} | Género: {genero} | Estado: {estado} >"
                        
                        print(formato)
                
                if opcion_listar == 1: # Listar por Estado
                    estado = input("Ingrese el estado del libro con el que desea listar: ")
                    lista_libros = biblioteca.listar_por_estado(estado) # devuelve una lista 
                    
                    if len(lista_libros) >= 1:
                        listar(lista_libros)
                    else:
                        print(f"No hay libros con el estado '{estado}'.")
                
                elif opcion_listar == 2: # Listar por Autor
                    
                    nombre = input("Ingrese el nombre del autor: ")
                    apellido = input("Ingrese el apellido del autor: ")
                    lista_libros = biblioteca.listar_por_autor(nombre, apellido)
                    
                    if len(lista_libros) >= 1:
                        listar(lista_libros)
                    else:
                        print(f"No hay libros registrados para el autor autor '{nombre} {apellido}'.")
                
                elif opcion_listar == 3: # Listar por area del conocimiento
                    
                    area_del_conocimiento = input("Ingrese el área del conocimiento: ")
                    lista_libros = biblioteca.listar_por_area_del_conocimiento(area_del_conocimiento)
                
                    if len(lista_libros) >= 1:
                        listar(lista_libros)
                    else:
                        print(f"No hay libros registrados cuya área del conocimiento sea '{area_del_conocimiento}'.")
                    
                elif opcion_listar == 4: # Listar por genero
                    
                    genero = input("Ingrese el género: ")
                    lista_libros = biblioteca.listar_por_genero(genero)
                    
                    if len(lista_libros) >= 1:
                        listar(lista_libros)
                    else:
                        print(f"No hay libros registrados cuyo género sea '{genero}'.")
                
                elif opcion_listar == 5: # Listar por año de publicacion
                    
                    anio_publicacion = input("Ingrese el año de publicación: ")
                    lista_libros = biblioteca.listar_por_anio_publicacion(anio_publicacion)
                    
                    if len(lista_libros) >= 1:
                        listar(lista_libros)
                    else:
                        print(f"No hay libros registrados para el año de publicación '{anio_publicacion}'.")
                    
                else:
                    print(f"Opción {opcion} no válida. Por favor, intente nuevamente.")
                
            elif opcion == 8: # Volver al menu principal
                break

            else:
                print(f"Opción {opcion} no válida. Por favor, intente nuevamente.")

    def gestionar_lectores(biblioteca:Biblioteca):
        
        while True:
            
            Main.mostrar_menu_lectores()
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1: # Agregar Lector
                
                nombre = input("Ingrese el nombre del lector: ")
                apellido = input("Ingrese el apellido del lector: ")
                identificacion = input("Ingrese la identificación del lector: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del lector en el formato DD/MM/Y: ")
                email = input("Ingrese el correo electrónico del lector: ")
                
                if biblioteca.agregar_lector(nombre, apellido, fecha_nacimiento, identificacion, email) == True:
                    print(f"Lector con identificación {identificacion} agregagdo exitosamente.")
                else:
                    print(f"El lector con identificación {identificacion} ya está registrado.")
                
            elif opcion == 2: # Eliminar Lector
                
                identificacion= input("Ingrese la identificación del lector: ")
                if biblioteca.eliminar_lector(identificacion) == True:
                    print(f"Lector con identificación {identificacion} eliminado exitosamente.")
                else:
                    print(f"No se pudo eliminar al lector con identificación {identificacion}. No está registrado en el sistema. ")

            elif opcion == 3: # Buscar Lector
                
                identificacion = input("Ingrese la identificación del lector: ")
                lector = biblioteca.buscar_lector(identificacion)
                
                if lector is not None:
                    print("\nLector encontrado: \n")
                    print(lector)
                else:
                    print(f"\nLector con identificación '{identificacion}' no encontrado.\n")

            elif opcion == 4: # Listar Préstamos del lector
                
                identificacion_lector = input("Ingrese la identificación del lector: ")
                lector = biblioteca.buscar_lector(identificacion_lector)
                
                if lector is not None:
                    
                    prestamos = lector.get_prestamos() # retorna una lista
                    prestamos_validos = [prestamo for prestamo in prestamos if prestamo is not None]
                    
                    if len(prestamos_validos) > 0:
                        print(f"\nPréstamos del lector con identificación {identificacion_lector}: \n")
                        for prestamo in prestamos:
                            print(prestamo)
                    else:
                        print(f"\nEl lector '{identificacion_lector}' no ha realizado préstamos.\n")
                else:
                    print(f"\nLector con identificación '{identificacion_lector}' no encontrado.\n")
            
            elif opcion == 5: # Listar Multas del lector
                
                identificacion_lector = input("Ingrese la identificación del lector: ")
                lector = biblioteca.buscar_lector(identificacion_lector)
                
                if lector is not None:
                
                    multas = lector.get_multas() # retorna un ndarray
                    
                    # Verificar si hay al menos un objeto que no sea None
                    if np.any(multas is not None): # Esto devuelve True si hay algún elemento no None
                        print(f"\nMultas del lector {identificacion_lector}: \n")
                        for multa in multas:
                            if multa is not None:
                                print(multa)
                    else:
                        print(f"\nEl lector '{identificacion_lector}' no tiene multas.\n")
            
            elif opcion == 6: # Listar Recibos del lector
                
                identificacion_lector = input("Ingrese la identificación del lector: ")
                lector = biblioteca.buscar_lector(identificacion_lector)
                
                if lector is not None:
                    
                    recibos = lector.get_recibos()
                    
                    if any(recibo is not None for recibo in recibos):
                        print(f"\nRecibos del lector {identificacion_lector}: \n")
                        for recibo in recibos:
                            if recibo is not None:
                                print(recibo)
                    else:
                        print(f"\nEl lector '{identificacion_lector}' no tiene recibos.\n")
                else:
                    print(f"\nLector '{identificacion_lector}' no encontrado.\n")
            
            elif opcion == 7: # Listar Préstamos Vigentes del Lector
                
                identificacion_lector = input("Ingrese la identificación del lector: ")
                lector = biblioteca.buscar_lector(identificacion_lector)
                
                if lector is not None:
                    prestamos_vigentes = lector.get_prestamos_vigentes()
                    
                    if np.any(prestamos is not None):
                        print(f"\nPrestamos vigentes del lector {identificacion_lector}: \n")
                        for prestamo in prestamos_vigentes:
                            if prestamo is not None:
                                print(prestamo)
                    else:
                        print(f"\nEl lector '{identificacion_lector}' no tiene prestamos vigentes.")
                else:
                    print(f"\nLector '{identificacion_lector}' no encontrado.\n")
            
            elif opcion == 8: # Consultar nro de Multas
                
                identificacion_lector = input("Ingrese la identificación del lector: ")
                lector = biblioteca.buscar_lector(identificacion_lector)
                
                if lector is not None:
                    print(f"\nEl lector {identificacion_lector} tiene {lector.get_nro_multas()} multas.")
                else:
                    print(f"\nLector '{identificacion_lector}' no encontrado.\n")
            
            elif opcion == 9: # Consultar nro Prestamos vigentes
                
                identificacion_lector = input("Ingrese la identificación del lector: ")
                lector = biblioteca.buscar_lector(identificacion_lector)
                
                if lector is not None:
                    print(f"\nEl lector {identificacion_lector} tiene {lector.get_nro_prestamos_vigentes()} prestamos vigentes.")
                else:
                    print(f"\nLector '{identificacion_lector}' no encontrado.\n")
                
            elif opcion == 10: # Volver al menú principal
                break

            else:
                print(f"Opción {opcion} no válida. Por favor, intente nuevamente.")    

    def gestionar_bibliotecarios(biblioteca:Biblioteca):
        
        while True:
            
            Main.mostrar_menu_bibliotecarios()
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1: # Agregar Bibliotecario
                
                nombre= input("Ingrese el nombre del bibliotecario: ")
                apellido=input("Ingrese el apellido del bibliotecario: ")
                fecha_nacimiento=input("Ingrese la fecha de nacimiento del bibliotecario (DD/MM/Y)")
                identificacion= input("Ingrese la identificación del bibliotecario: ")
                email= input("Ingrese el email del bibliotecario: ")  
                
                if biblioteca.agregar_bibliotecario(nombre, apellido, fecha_nacimiento, identificacion, email) == True:
                    print(f"Bibliotecario con identificación {identificacion} registrado exitosamente.")
                else:
                    print(f"El Bibliotecario con identificación {identificacion} ya está registrado.")
                
            elif opcion == 2: # Eliminar Bibliotecario
                
                identificacion= input("Ingrese la identificación del bibliotecario: ")
                if biblioteca.eliminar_bibliotecario(identificacion) == True:
                    print(f"Bibliotecario con identificación {identificacion} eliminado exitosamente.")
                else:
                    print(f"No se pudo eliminar al Bibliotecario con identificación {identificacion}. No está registrado en el sistema.")

            elif opcion == 3: # Buscar Bibliotecario
                
                identificacion = input("Ingrese la identificación del bibliotecario: ")
                bibliotecario = biblioteca.buscar_lector(identificacion)
                
                if bibliotecario is not None:
                    print("\nBibliotecario encontrado: \n")
                    print(bibliotecario)
                else:
                    print(f"\nBibliotecario con identificación '{identificacion}' no encontrado.\n")
                
            elif opcion == 4: # Volver al menú principal
                break

            else:
                print(f"Opción {opcion} no válida. Por favor, intente nuevamente.")

    def gestionar_autores(biblioteca:Biblioteca):
        
        while True:
            
            Main.mostrar_menu_autores()
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1: # Agregar Autor
                
                nombre = input("Ingrese el nombre del autor: ")
                apellido = input("Ingrese el apellido del autor: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del autor (DD/MM/Y): ")
                fecha_fallecimiento = input("Ingrese la fecha de fallecimiento del autor (DD/MM/Y): ")
                pais_origen = input("Ingrese el pais de origen del autor: ")
                
                if biblioteca.agregar_autor(nombre,apellido,fecha_nacimiento,fecha_fallecimiento,pais_origen) == True:
                    print(f"Autor '{nombre} {apellido}' agregado exitosamente.")
                else:
                    print(f"El autor '{nombre} {apellido}' ya está registrado en el sistema.")
                
            elif opcion == 2: # Eliminar autor
                
                nombre= input("Ingrese el nombre del autor: ")
                apellido=input("Ingrese el apellido del autor: ")
                
                if biblioteca.eliminar_autor(nombre,apellido) == True:
                    print(f"Autor '{nombre} {apellido}' eliminado exitosamente.")
                else:
                    print(f"El autor '{nombre} {apellido}' no está registrado. No se pudo eliminar.")
    
            elif opcion == 3: # Buscar autor
                
                nombre= input("Ingrese el nombre del autor: ")
                apellido=input("Ingrese el apellido del autor: ")
                
                autor = biblioteca.buscar_autor(nombre,apellido)
                
                if autor is not None:
                    print("\nAutor encontrado: \n")
                    print(autor)
                else:
                    print(f"Autor '{nombre} {apellido}' no encontrado.")
                
            elif opcion == 4: # Volver al menu principal
                break

            else:
                print(f"Opción {opcion} no válida. Por favor, intente nuevamente.")      
    
    def guardar_y_salir(biblioteca:Biblioteca):
        Main.guardar_biblioteca(biblioteca)
        
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