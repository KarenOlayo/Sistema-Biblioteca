import numpy as np
from Libro import Libro
from Lector import Lector

class Inventario:
    
    def __init__(self):
        self.__libros = np.full((500), fill_value=None , dtype=object)
        self.__nro_libros = 0
        self.__libros_prestados = []
        self.__libros_disponibles = []
    
    def listar_por_estado(self,estado):
        for i in range(0,self.__nro_libros,1):
            if self.__libros[i] is not None and self.__libros[i].get_estado() == estado:
                if estado == "Disponible" :
                    self.__libros_disponibles.append(self.__libros[i])
                elif estado == "Prestado":
                    self.__libros_prestados.append(self.__libros[i])
                
    def buscar_libro(self, titulo, codigo_isbn): 
        for i in range(0, self.__nro_libros, 1):
            if self.__libros[i] is not None and self.__libros[i].get_titulo() == titulo or self.__libros[i].get_codigo_isbn() == codigo_isbn:
                return i
            else:
                return -1

    def agregar_libro(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen, estado="Disponible"):
        
        libro = Libro(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen, estado)
        
        if self.__libros.buscar_libro(self, titulo, codigo_isbn) == -1:
            if self.__nro_libros < len(self.__libros):
                self.__libros[self.__nro_libros] = libro
                self.__nro_libros += 1
                self.agregar_libro_estante(area_del_conocimiento, libro)
                    
            else:
                libro.self__nro_ejemplares += nro_ejemplares
                self.__nro_libros += nro_ejemplares
                self.agregar_libro_estante(self, area_del_conocimiento, libro)
                
    def agregar_libro_estante(self, area_del_conocimiento, libro:object):
        
        estante = self.__estantes.buscar_estante(area_del_conocimiento) #retorna un objeto
        
        titulo = libro.get_titulo()
        codigo_isbn = libro.get_codigo_isbn()
        posicion_libro = self.buscar_libro(self, titulo, codigo_isbn)
        
        if estante.get_nro_libros_estante() < len(estante):
            if posicion_libro == -1 : 
                self.__libros_estante[self.__nro_libros_estante] = libro
                self.__nro_libros_estante += self.__nro_ejemplares
            else: 
                self.__nro_libros_estante += self.__nro_ejemplares

    def retirar_libro(self, titulo, codigo_isbn):
        
        # se valida si el libro existe en el inventario
        
        posicion_libro = self.buscar_libro(titulo, codigo_isbn)
        if posicion_libro != -1:
            for i in range(posicion_libro, self.__nro_libros, 1):
                self.__libros[i] = self.__libros[i+1]
            self.__libros[i+1] == None
            self.__nro_libros -= 1

        # modificar para si se retira un libro y todos sus ejemplares o solo un ejemplar

    def prestar_libro(self,titulo,codigo_isbn, lector:Lector):
        if lector.verificar_requisitos_prestamo() == True:
            posicion_libro = self.__libros.buscar_libro(self,titulo, codigo_isbn)
            if posicion_libro != -1:
                self.__libros[posicion_libro].set_estado("Prestado")
                self.__libros_prestados.append(self.__libros[posicion_libro])
                lector.get_prestamos_vigentes().append()
                
                for i in self.__libros_disponibles:
                    if self.__libros_disponibles[i].get_titulo() == titulo and self.__libros_disponibles[i].get_codigo_isbn() == codigo_isbn:
                        self.__libros_disponibles.pop(i)

    def renovar_prestamo(self):
        pass

    def reservar_libro(self):
        pass

    def recibir_libro_devuelto(self):
        pass