from DataInicial import AREAS_DEL_CONOCIMIENTO
from DataInicial import GENEROS_LITERATURA
from DataInicial import GENEROS_NO_LITERATURA
from DataInicial import ORIGEN_LIBRO
from DataInicial import ESTADO_LIBRO
from datetime import datetime


class Libro:
    
    def __init__(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, fecha_publicacion, origen, estado="Disponible"):
          
        self.__titulo = titulo
        self.__codigo_isbn = codigo_isbn
        self.__estado = estado
        self.__autor = autor
        
        if area_del_conocimiento in AREAS_DEL_CONOCIMIENTO:
            self.__area_del_conocimiento = area_del_conocimiento
                
            if area_del_conocimiento == "Literatura":
                if genero in GENEROS_LITERATURA:
                    self.__genero = genero
            else:
                if genero in GENEROS_NO_LITERATURA:
                    self.__genero = genero
        
        if origen in ORIGEN_LIBRO:
            self.__origen = origen
        
        if estado in ESTADO_LIBRO:
            self.__estado = estado
            
        self.__nro_paginas = nro_paginas
        self.__fecha_publicacion = fecha_publicacion
  
    #Metodos accesores

    def get_titulo(self):
        return self.__titulo

    def get_codigo_isbn(self):
        return self.__codigo_isbn

    def get_autor(self):
        return self.__autor

    def get_area_del_conocimiento(self):
        return self.__area_del_conocimiento

    def get_genero(self):
        return self.__genero

    def get_nro_paginas(self):
        return self.__nro_paginas

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion

    def  get_origen(self):
        return self.__origen

    def get_estado(self):
        return self.__estado

    #Metodos Modificadores

    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def  set_codigo_isbn(self, nuevo_codigo_isbn):
        self.__codigo_isbn = nuevo_codigo_isbn

    def   set_area_del_conocimiento(self, nueva_area_del_conocimiento):
        self.__area_del_conocimiento = nueva_area_del_conocimiento

    def set_genero(self, nuevo_genero):
        self.__genero = nuevo_genero

    def set_nro_paginas(self,nuevo_nro_paginas):
        self.__nro_paginas = nuevo_nro_paginas

    def  set_fecha_publicacion(self, nueva_fecha_publicacion):
        self.__fecha_publicacion = nueva_fecha_publicacion

    def set_origen(self, nuevo_origen):
        self.__origen = nuevo_origen

    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado
    
    # Metodo representacion
    
    def __repr__(self):
        return f"('{self.__titulo}', '{self.__codigo_isbn}', '{self.__autor}')"