class Libro:
    
    AREAS_DEL_CONOCIMIENTO = [
        "Ciencias Sociales",
        "Ciencias Humanas",
        "Ciencias Exactas",
        "Ciencias Políticas",
        "Literatura"
    ]
    
    GENEROS_LITERATURA = [
    "Ciencia Ficción",
    "Fantasía",
    "Romance",
    "Aventura",
    "Comedia",
    "Infantil",
    "Religioso",
    "Poesía",
    "Ilustrado"
    ]

    GENEROS_NO_LITERATURA = [
    "Ensayo",
    "Didáctico",
    "Investigación",
    "Histórico",
    "Práctico",
    "Diccionario",
    "Enciclopedia"
    ]

    ORIGEN_LIBRO = ["Donacion","Adquirido por la Biblioteca"]
    
    def __init__(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, nro_ejemplares, fecha_publicacion, editorial, origen):
        
        self.__titulo = titulo
        self.__codigo_isbn = codigo_isbn
        self.__autor = [] #¿Se debe almacenar en una lista, indicar el nombre directamente o ...?

        
        if area_del_conocimiento in Libro.AREAS_DEL_CONOCIMIENTO:
            self.__area_del_conocimiento = area_del_conocimiento
                
            if area_del_conocimiento == "Literatura":
                if genero in Libro.GENEROS_LITERATURA:
                    self.__genero = genero
            else:
                if genero in Libro.GENEROS_NO_LITERATURA:
                    self.__genero = genero
            
        self.__nro_paginas = nro_paginas
        self.__nro_ejemplares = nro_ejemplares
        self.__fecha_publicacion = fecha_publicacion
        self.__editorial = editorial
        
        if origen in Libro.ORIGEN_LIBRO:
            self.__origen = origen

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

def get_nro_ejemplares(self):
    return self.__nro_ejemplares

def get_fecha_publicacion(self):
    return self.__fecha_publicacion

def get_editorial(self):
    return self.__editorial

def  get_origen(self):
    return self.__origen

#Metodos Modificadores

def set_titulo(self, nuevo_titulo):
    self.__titulo = nuevo_titulo

def  set_codigo_isbn(self, nuevo_codigo_isbn):
    self.__codigo_isbn = nuevo_codigo_isbn

def  set_autor(self, nuevo_autor):
    self.__autor = nuevo_autor

def   set_area_del_conocimiento(self, nueva_area_del_conocimiento):
    self.__area_del_conocimiento = nueva_area_del_conocimiento

def set_genero(self, nuevo_genero):
    self.__genero = nuevo_genero

def set_nro_paginas(self,nuevo_nro_paginas):
    self.__nro_paginas = nuevo_nro_paginas

def  set_nro_ejemplares(self, nuevo_nro_ejemplares):
    self.__nro_ejemplares = nuevo_nro_ejemplares

def  set_fecha_publicacion(self, nueva_fecha_publicacion):
    self.__fecha_publicacion = nueva_fecha_publicacion

def set_editorial(self, nueva_editorial):
    self.__editorial = nueva_editorial

def set_origen(self, nuevo_origen):
    self.__origen = nuevo_origen