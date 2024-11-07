import numpy as np
from Libro import Libro

class Inventario:
    
    def __init__(self):
        self.__libros = np.full((500), fill_value=None , dtype=object)
        self.__nro_libros = 0
        self.__libros_prestados = []
        self.__libros_disponibles = []
        self.__libros_reservados = []
        
def buscar_libro(self, titulo, codigo_isbn): 
    for i in range(0, self.__nro_libros, 1):
        if self.__libros[i] is not None and self.__libros[i].get_titulo() == titulo or self.__libros[i].get_codigo_isbn() == codigo_isbn:
            return i
        else:
            return -1

#¿seria recomendable hacer un metodo de busqueda por cada criterio de forma independiente?
#¿buscar solo con isbn?
#¿almacenar los resultados en una lista?
#¿hacer metodos para listar por autor, genero, area del conocimiento, año publicacion?

def agregar_libro(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, nro_ejemplares, fecha_publicacion, editorial, origen):
    
    libro = Libro(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, nro_ejemplares, fecha_publicacion, editorial, origen)
    
    if self.__libros.buscar_libro(self, titulo, codigo_isbn) == -1: # no esta registrado
        if self.__nro_libros < len(self.__libros):
            
            self.__libros[self.__nro_libros] = libro # se agrega el libro al arreglo de libros de la biblioteca
            self.__nro_libros += 1
            
            self.agregar_libro_estante(area_del_conocimiento, libro) # se agrega el libro al estante correspondiente
                
        else:
            libro.self__nro_ejemplares += nro_ejemplares # se aumenta el nro de ejemplares y el nro de libros en el inventario
            self.__nro_libros += nro_ejemplares
            
            self.agregar_libro_estante(self, area_del_conocimiento, libro) # se aumenta el nro de libros en el estante 

def agregar_libro_estante(self, area_del_conocimiento, libro:object):
    
    estante = self.__estantes.buscar_estante(area_del_conocimiento) #retorna un objeto
    
    titulo = libro.get_titulo()
    codigo_isbn = libro.get_codigo_isbn()
    posicion_libro = self.buscar_libro(self, titulo, codigo_isbn)
    
    if estante.get_nro_libros_estante() < len(estante):
        if posicion_libro == -1 : #si el libro no esta registrado
            self.__libros_estante[self.__nro_libros_estante] = libro
            self.__nro_libros_estante += self.__nro_ejemplares
        else: #si el libro esta registrado
            self.__nro_libros_estante += self.__nro_ejemplares

def retirar_libro(self, titulo, codigo_isbn):
    
    # se valida si el libro existe en el inventario
    
    posicion_libro = self.buscar_libro(titulo, codigo_isbn)
    if posicion_libro != -1:
        for i in range(posicion_libro, self.__nro_libros, 1):
            self.__libros[i] = self.__libros[i+1]
        self.__libros[i-1] == None
        self.__nro_libros -= 1

# modificar para si se retira un libro y todos sus ejemplares o solo un ejemplar

def prestar_libro(self):
    pass

def renovar_prestamo(self):
    pass

def reservar_libro(self):
    pass

def recibir_libro_devuelto(self):
    pass