import numpy as np
from Libro import Libro
from Lector import Lector
from Biblioteca import Biblioteca
from Prestamo import  Prestamo
from datetime import datetime , timedelta

class Inventario:
    
    def __init__(self, biblioteca:Biblioteca):
        self.__biblioteca = biblioteca
        self.__libros = np.full((500), fill_value=None , dtype=Libro)
        self.__nro_libros = 0
        self.__libros_prestados = []
        self.__libros_disponibles = []

    # Metodos de busqueda y verificacion
    
    def buscar_libro_biblioteca(self, titulo, codigo_isbn): 
        for indice, libro in enumerate(self.__libros):
            if indice >= self.__nro_libros: #¿>= o > ?
                break
            if libro is not None and libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                return indice, libro # retorna el indice y el objeto
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
            else:
                return None

    # Metodos de agregacion
    
    def agregar_libro_biblioteca(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen, estado="Disponible"):
        _, libro = self.buscar_libro_biblioteca(titulo, codigo_isbn)
        if libro is None:
            autor = self.verificar_autor(autor)
            if autor is not None:
                if self.__nro_libros < len(self.__libros):
                    libro = Libro(titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen, estado)
                    self.__libros[self.__nro_libros] = libro 
                    self.__nro_libros += 1 
                    self.agregar_libro_estante(area_del_conocimiento, libro)
                    print("Libro agregado con éxito.")
            else:
                print("El autor no está registrado.")
        else:
            print("El libro ya existe.")
                
    def agregar_libro_estante(self, area_del_conocimiento, libro:object):
        _, estante = self.__biblioteca.buscar_estante(area_del_conocimiento) #buscar estante es metodo de la clase Biblioteca
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
            titulo = libro.get_titulo()
            codigo_isbn = libro.get_codigo_isbn()
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
    
    def eliminar_libro_prestado(self, libro:object):
        self.__libros_prestados.remove(libro)
                
    # Metodos funcionales
    
    def prestar_libro(self,titulo,codigo_isbn, identificacion_lector, fecha_prestamo):
        lector = self.__biblioteca.buscar_lector(identificacion_lector) #retorna un objeto
        if lector is not None:
            if lector.verificar_requisitos_prestamo() == True:
                indice, libro = self.buscar_libro_biblioteca(titulo, codigo_isbn)
                if indice != -1:
                    if libro.get_estado() == "Disponible":
                        
                        codigo_prestamo = f"P{self.__biblioteca.get_nro_prestamos_biblioteca()}"
                        prestamo = Prestamo(codigo_prestamo, lector, libro, fecha_prestamo)
                        self.__biblioteca.agregar_prestamo(prestamo)
                        lector.get_prestamos().append(prestamo)
                        lector.agregar_libro_a_prestamos_vigentes(libro)
                        
                        libro.set_estado("Prestado")
                        self.eliminar_libro_disponible(titulo, codigo_isbn)
                        self.agregar_libro_prestado(libro)
                        
                        recibo =self.__biblioteca.generar_recibo(prestamo,identificacion_lector)
                        lector.guardar_recibo(recibo)
                        
                        print("Préstamo realizado con éxito.")
                        print(recibo)
                    
                    else:
                        print("El libro no está disponible.")
                else:
                    print("El libro no existe.")
            else:
                print("El lector no cumple con los requisitos.")
        else:
            print("El lector no está registrado.")
        
    def renovar_prestamo(self, codigo_prestamo, identificacion_lector):
        lector = self.__biblioteca.buscar_lector(identificacion_lector)
        prestamo = self.__biblioteca.buscar_prestamo(codigo_prestamo)
        estado_prestamo = prestamo.get_estado_prestamo()
        
        if lector is not None:
            if prestamo is not None and estado_prestamo == "Vigente":
                cumple_requisitos = lector.verificar_requisitos_renovacion()
                if cumple_requisitos == True:
                    fecha_devolucion_inicial = prestamo.get_fecha_devolucion()
                    nueva_fecha_devolucion = fecha_devolucion_inicial + timedelta(days=30)
                    prestamo.set_fecha_devolucion(nueva_fecha_devolucion)
                    prestamo.incrementar_nro_renovaciones()
    
    def recibir_libro_devuelto(self, codigo_prestamo, identificacion_lector, fecha_entrega):
        lector = self.__biblioteca.buscar_lector(identificacion_lector)
        prestamo = self.__biblioteca.buscar_prestamo(codigo_prestamo)
        if lector is not None:
            if prestamo is not None:
                if prestamo.get_lector().get_identificacion() == identificacion_lector:
                    libro = prestamo.get_libro()
                    if libro is not None:
                        libro.set_estado("Disponible")
                        
                        for libro in self.__libros_prestados:
                            if libro.get_codigo_isbn() == prestamo.get_libro().get_codigo_isbn():
                                self.eliminar_libro_prestado(libro)
                        self.agregar_libro_disponible(libro)
                    
                    lector.eliminar_libro_de_prestamos_vigentes(libro)                    
                    
                    prestamo.set_fecha_entrega(fecha_entrega)
                    prestamo.set_estado("Terminado")
                    
                    multa = self.__biblioteca.calcular_multa(prestamo)
                    
                    recibo = self.__biblioteca.generar_recibo(multa, identificacion_lector)
                    print(recibo)
                    
                    print("Libro devuelto exitosamente.")
                    
                else:
                    print(f"El prestamo {codigo_prestamo} no corresponde al lector {identificacion_lector}")
            else:
                print(f"El prestamo {codigo_prestamo} no existe.")
        else:
            print(f"El lector {identificacion_lector} no existe.")
            
    # Metodos para listar
    
    def listar_por_estado(self,estado):
        for i in range(0,self.__nro_libros,1):
            if self.__libros[i] is not None and self.__libros[i].get_estado() == estado:
                if estado == "Disponible" :
                    self.__libros_disponibles.append(self.__libros[i])
                elif estado == "Prestado":
                    self.__libros_prestados.append(self.__libros[i])
    
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
    
    def listar_por_fecha_publicacion(self):
        pass