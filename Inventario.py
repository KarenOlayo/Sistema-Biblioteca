import numpy as np
from Libro import Libro
from Biblioteca import Biblioteca
from datetime import datetime , timedelta
import csv

class Inventario:
    
    def __init__(self, biblioteca:Biblioteca):
        self.__biblioteca = biblioteca
        self.__libros = np.full((500), fill_value=None , dtype=Libro)
        self.__nro_libros = 0
        self.__libros_prestados = []
        self.__libros_disponibles = []
    
    @property
    def get_biblioteca(self):
        return self.__biblioteca

    # Metodos de busqueda y verificacion
    
    def buscar_libro_biblioteca(self, titulo, codigo_isbn): 
        for indice, libro in enumerate(self.__libros):
            if indice >= self.__nro_libros: #¿>= o > ?
                break
            if libro is not None and libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                return indice, libro 
        return -1 , None 
    
    def buscar_libro_disponible(self, titulo, codigo_isbn):
        for libro in self.__libros_disponibles:
            if libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                return libro
        return None
    
    def buscar_libro_prestado(self, titulo, codigo_isbn):
        for libro in self.__libros_prestados:
            if libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                return libro
        return None
        
    def verificar_autor(self, autor:str): # se ingresa el nombre y apellido del autor separado por espacio
        nombre_apellido = autor.split()
        if len(nombre_apellido) == 2:
            nombre, apellido = nombre_apellido
            obj_autor = self.__biblioteca.buscar_autor(nombre, apellido)
            if obj_autor is not None:
                return obj_autor
        return None

    # Metodos de agregacion
    
    def agregar_libro_biblioteca(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen):
        _, libro = self.buscar_libro_biblioteca(titulo, codigo_isbn)
        if libro is None:
            autor_valido = self.verificar_autor(autor)
            if autor_valido is not None:
                if self.__nro_libros < len(self.__libros):
                    libro = Libro(titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen)
                    self.__libros[self.__nro_libros] = libro 
                    self.__nro_libros += 1 
                    self.agregar_libro_estante(area_del_conocimiento, libro)
                    print("Libro agregado con éxito.")
            else:
                print("El autor no está registrado.")
        else:
            print("El libro ya existe.")
                
    def agregar_libro_estante(self, area_del_conocimiento, libro:Libro):
        _, estante = self.__biblioteca.buscar_estante(area_del_conocimiento)
        if estante is not None:
            if estante.get_nro_libros_estante() < len(estante.get_libros_estante()):
                estante.get_libros_estante()[estante.get_nro_libros_estante()] = libro
                estante.incrementar_nro_libros_estante() #suma 1 al nro de libros del estante
    
    def agregar_libro_disponible(self, libro=Libro):
        titulo = libro.get_titulo()
        codigo_isbn = libro.get_codigo_isbn()
        
        if self.buscar_libro_disponible(titulo, codigo_isbn) is None:
            self.__libros_disponibles.append(libro)
            return True
        return False
    
    def agregar_libro_prestado(self, libro=Libro):
        titulo = libro.get_titulo()
        codigo_isbn = libro.get_codigo_isbn()
        
        if self.buscar_libro_prestado(titulo, codigo_isbn) is None:
            self.__libros_prestados.append(libro)
            return True
        return False

    # Metodos de eliminacion
    
    def eliminar_libro_biblioteca(self, titulo, codigo_isbn):        
        indice, libro = self.buscar_libro_biblioteca(titulo, codigo_isbn)
        if libro is not None:
            area_del_conocimiento = libro.get_area_del_conocimiento()
            _, estante = self.__biblioteca.buscar_estante(area_del_conocimiento)
            if indice != -1:
                for i in range(indice, self.__nro_libros-1):
                    self.__libros[i] = self.__libros[i+1]
                self.__libros[self.__nro_libros-1] = None 
                self.__nro_libros -= 1
            
                estante.eliminar_libro_estante(titulo, codigo_isbn)
                print("Libro eliminado de la biblioteca.")
                
    def eliminar_libro_disponible(self, titulo, codigo_isbn):
        for libro in self.__libros_disponibles:
            if libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                self.__libros_disponibles.remove(libro)
    
    def eliminar_libro_prestado(self, titulo, codigo_isbn):
        for libro in self.__libros_prestados:
            if libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                self.__libros_prestados.remove(libro)
                
    # Metodos funcionales
    
    def prestar_libro(self, titulo, codigo_isbn, identificacion_lector, fecha_prestamo):
        lector = self.__biblioteca.buscar_lector(identificacion_lector) #retorna un objeto
        
        if lector is None:
            print(f"No se puede realizar el préstamo. Lector {identificacion_lector} no encontrado.")
            return
        
        lector_cumple_requisitos = lector.verificar_requisitos_prestamo()
        
        if lector_cumple_requisitos == False:
            print(f"No se puede realizar el préstamo. Lector {identificacion_lector} no cumple con los requisitos para el préstamo.")
            return
        
        indice, libro = self.buscar_libro_biblioteca(titulo, codigo_isbn)
        
        if indice == -1 and libro is None:
            print(f"No se puede realizar el préstamo. Libro {titulo} no encontrado.")
            return
        
        if libro.get_estado() == "Disponible":
            
            libro.set_estado("Prestado")
    
            prestamo = self.__biblioteca.generar_prestamo(lector, libro, fecha_prestamo)
            recibo = self.__biblioteca.generar_recibo(prestamo, lector)
            
            self.__biblioteca.guardar_prestamo(prestamo)
            self.__biblioteca.guardar_recibo(recibo)
                            
            lector.guardar_prestamo(prestamo)
            lector.guardar_recibo(recibo)
            lector.agregar_libro_a_prestamos_vigentes(libro)
            
            self.eliminar_libro_disponible(titulo, codigo_isbn)
            self.agregar_libro_prestado(libro)
                
            print("Préstamo realizado con éxito.")
            #print(recibo)
        
    def renovar_prestamo(self, codigo_prestamo, identificacion_lector):
        lector = self.__biblioteca.buscar_lector(identificacion_lector)
        prestamo = self.__biblioteca.buscar_prestamo(codigo_prestamo)
        
        if prestamo is None:
            print(f"El préstamo {codigo_prestamo} no existe. No se pudo renovar el préstamo.")
            return
        
        estado_prestamo = prestamo.get_estado_prestamo()
        
        if lector is not None:
            if prestamo is not None and estado_prestamo == "Vigente":
                cumple_requisitos = lector.verificar_requisitos_renovacion(codigo_prestamo)
                if cumple_requisitos == True:
                    fecha_devolucion_inicial = prestamo.get_fecha_devolucion()
                    nueva_fecha_devolucion = fecha_devolucion_inicial + timedelta(days=30)
                    prestamo.set_fecha_devolucion(nueva_fecha_devolucion)
                    prestamo.incrementar_nro_renovaciones()
                    prestamo.set_estado("Renovado")
                    
                    recibo = self.__biblioteca.generar_recibo(prestamo, lector)
                    self.__biblioteca.guardar_recibo(recibo)
                    lector.guardar_recibo(recibo)
                    
                    print("Prestamo renovado exitosamente.")
                    #print(recibo)
    
    def recibir_libro_devuelto(self, codigo_prestamo, identificacion_lector, fecha_entrega):
        lector = self.__biblioteca.buscar_lector(identificacion_lector)
        prestamo = self.__biblioteca.buscar_prestamo(codigo_prestamo)
        
        if prestamo is None:
            print(f"El préstamo {codigo_prestamo} no existe")
            return
        
        fecha_prestamo  = prestamo.get_fecha_prestamo()
        
        if datetime.strptime(fecha_entrega, '%d/%m/%Y').date() >= fecha_prestamo:
            if lector is not None:
                if prestamo is not None:
                    if prestamo.get_lector().get_identificacion() == identificacion_lector:
                        libro = prestamo.get_libro()
                        if libro is not None:
                            libro.set_estado("Disponible")
                            
                            self.eliminar_libro_prestado(libro.get_titulo(),libro.get_codigo_isbn())
                            self.agregar_libro_disponible(libro)
                        
                            lector.eliminar_libro_de_prestamos_vigentes(libro)                    
                        
                            prestamo.set_fecha_entrega(fecha_entrega)
                            prestamo.set_estado("Terminado")
                                                        
                            multa = self.__biblioteca.calcular_multa(prestamo, lector)
                            if multa is not None:
                                prestamo.set_multa(multa)
                                lector.guardar_multa(multa)
                                self.__biblioteca.guardar_multa(multa)
                                #print(multa)
                                
                                recibo_multa = self.__biblioteca.generar_recibo(multa, lector)
                                self.__biblioteca.guardar_recibo(recibo_multa)
                                lector.guardar_recibo(recibo_multa)
                                #print(recibo_multa)
                            
                            recibo_devolucion = self.__biblioteca.generar_recibo(prestamo,lector)
                            self.__biblioteca.guardar_recibo(recibo_devolucion)
                            lector.guardar_recibo(recibo_devolucion)
                            print("Libro devuelto exitosamente.")
                            #print(recibo_devolucion)
                            
                        else:
                            print(f"El libro no existe")
                    else:
                        print(f"El prestamo {codigo_prestamo} no corresponde al lector {identificacion_lector}")
                else:
                    print(f"El prestamo {codigo_prestamo} no existe.")
            else:
                print(f"El lector {identificacion_lector} no existe.")
        else:
            print("La fecha de entrega es anterior a la fecha de prestamo.")
            
    # Metodos para listar
    
    def listar_por_estado(self,estado):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro] is not None and self.__libros[libro].get_estado() == estado:
                if estado == "Disponible" :
                    listado_libros.append(self.__libros[libro])
                if estado == "Prestado" :
                    listado_libros.append(self.__libros[libro])
        return listado_libros
    
    def listar_por_autor(self, nombre, apellido):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro].get_autor().get_nombre() == nombre and self.__libros[libro].get_autor().get_apellido() == apellido:
                listado_libros.append(libro)
        return listado_libros
    
    def listar_por_area_del_conocimiento(self, area_del_conocimiento):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro].get_area_del_conocimiento() == area_del_conocimiento:
                listado_libros.append(libro)
        return listado_libros
    
    def listar_por_genero(self, genero):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro].get_genero() == genero:
                listado_libros.append(libro)
        return listado_libros
    
    def listar_por_fecha_publicacion(self, fecha_publicacion):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro].get_fecha_publicacion() == fecha_publicacion:
                listado_libros.append(libro)
        return listado_libros
    
    def crear_archivo_lectores(self):
        lectores_objeto = self.__biblioteca.get_lectores()
        datos_lectores = []
        columnas_lector = ["Identificacion","Nombre","Apellido"]
        for lector in lectores_objeto:
            datos_lectores.append([lector.get_identificacion(),lector.get_nombre(),lector.get_apellido()])
        print(datos_lectores)
        self.cargar_archivo("lectores.csv",columnas_lector,datos_lectores) 
    
    def crear_archivo_autores(self):
        autores_objeto = self.__biblioteca.get_autores()
        datos_autores = []
        columnas_autor = ["Nombre","Apellido","Pais de Origen"]
        for autor in autores_objeto:
            datos_autores.append([autor.get_nombre(),autor.get_apellido(),autor.get_pais_origen()])
        print(datos_autores)
        self.cargar_archivo("autores.csv",columnas_autor,datos_autores) 
            
    def cargar_archivo(self, nombre_archivo, columnas_a_guardar, filas_a_guardar):
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            if archivo.tell() == 0:
                escritor.writerow(columnas_a_guardar)
            
            for item in filas_a_guardar:
                escritor.writerow(item)
                print(item)
        