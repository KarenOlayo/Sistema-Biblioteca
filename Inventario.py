import numpy as np
from Libro import Libro
from Lector import Lector
from Biblioteca import Biblioteca

class Inventario:
    
    def __init__(self, biblioteca:Biblioteca):
        self.__biblioteca = biblioteca
        self.__libros = np.full((500), fill_value=None , dtype=object)
        self.__nro_libros = 0
        self.__libros_prestados = []
        self.__libros_disponibles = []

    # Metodos de busqueda
    
    def buscar_libro_biblioteca(self, titulo, codigo_isbn): 
        for indice, libro in enumerate(self.__libros):
            if indice >= self.__nro_libros: #¿>= o > ?
                break
            if libro is not None and (libro.get_titulo() == titulo or libro.get_codigo_isbn() == codigo_isbn):
                return indice, libro # retorna el indice y el objeto
        return -1 , None 

    # Metodos de agregacion
    
    def agregar_libro_biblioteca(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen, estado="Disponible"):
        _, libro = self.buscar_libro(titulo, codigo_isbn)
        if libro is None:
            if self.__nro_libros < len(self.__libros):
                libro = Libro(titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen, estado)
                self.__libros[self.__nro_libros] = libro 
                self.__nro_libros += 1 
                self.agregar_libro_estante(area_del_conocimiento, libro)
                
    def agregar_libro_estante(self, area_del_conocimiento, libro:object):
        _, estante = self.__biblioteca.buscar_estante(area_del_conocimiento) #buscar estante es metodo de la clase Biblioteca
        if estante is not None:
            if estante.get_nro_libros_estante() < len(estante.get_libros_estante()):
                estante.get_libros_estante()[estante.get_nro_libros_estante()] = libro
                estante.set_nro_libros_estante() #suma 1 al nro de libros del estante

    # Metodos de eliminacion
    
    def eliminar_libro(self, titulo, codigo_isbn):        
        indice, libro = self.buscar_libro_biblioteca(titulo, codigo_isbn)
        titulo = libro.get_titulo()
        codigo_isbn = libro.get_codigo_isbn()
        area_del_conocimiento = libro.get_area_del_conocimiento()
        estante = self.__biblioteca.buscar_estante(area_del_conocimiento)
        if indice != -1:
            for i in range(indice, self.__nro_libros, 1):
                self.__libros[i] = self.__libros[i+1]
            self.__libros[i+1] == None #se suma o se resta 1 ?
            self.__nro_libros -= 1    
        
        estante.eliminar_libro_estante(titulo, codigo_isbn)
                
    # Metodos funcionales
    
    def prestar_libro(self,titulo,codigo_isbn, lector:Lector):
        if lector.verificar_requisitos_prestamo() == True:
            indice, libro = self.buscar_libro(titulo, codigo_isbn)
            if indice != -1:
                self.__libros[indice].set_estado("Prestado")
                self.__libros_prestados.append(self.__libros[indice])
                lector.get_prestamos_vigentes().append(libro)
                print("Préstamo realizado con éxito.")
                
                for i in self.__libros_disponibles:
                    if self.__libros_disponibles[i].get_titulo() == titulo and self.__libros_disponibles[i].get_codigo_isbn() == codigo_isbn:
                        self.__libros_disponibles.pop(i)
        print("No se pudo realizar el préstamo.")
        
    def renovar_prestamo(self):
        pass

    def recibir_libro_devuelto(self):
        pass
    
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