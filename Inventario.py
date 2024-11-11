import numpy as np
from Libro import Libro
from Lector import Lector
from Biblioteca import Biblioteca

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
        for indice, libro in enumerate(self.__libros):
            if indice >= self.__nro_libros: #¿>= o > ?
                break
            if libro is not None and (libro.get_titulo() == titulo or libro.get_codigo_isbn() == codigo_isbn):
                return indice, libro # retorna el indice y el objeto
        return -1 , None 

    def agregar_libro(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen, estado="Disponible"):
        _, libro = self.buscar_libro(titulo, codigo_isbn)
        if libro is None:
            if self.__nro_libros < len(self.__libros):
                libro = Libro(titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen, estado)
                self.__libros[self.__nro_libros] = libro 
                self.__nro_libros += 1 
                self.agregar_libro_estante(area_del_conocimiento, libro)
                
    def agregar_libro_estante(self, area_del_conocimiento, libro:object):
        _, estante = self.buscar_estante(area_del_conocimiento) #buscar estante es metodo de la clase Biblioteca
        if estante is not None:
            if estante.get_nro_libros_estante() < len(estante.get_libros_estante()):
                estante.get_libros_estante()[estante.get_nro_libros_estante()] = libro
                estante.set_nro_libros_estante() #suma 1 al nro de libros del estante

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