import numpy as np
from DataInicial import AREAS_DEL_CONOCIMIENTO
class Estante:
    
    def __init__(self, area_del_conocimiento):
        
        if area_del_conocimiento in AREAS_DEL_CONOCIMIENTO:
                self.__area_del_conocimiento = area_del_conocimiento
        else:
                print(f"Área del conocimiento '{area_del_conocimiento}' no es válida.")
        
        self.__libros_estante = np.full((100), fill_value=None, dtype=object)
        self.__nro_libros_estante = 0
        
        #Pregunta: Como maximo, un estante tendra 100 libros ¿Se debera poner una variable con este valor,
        #para hacer la validacion a la hora de agregar un libro o hacerla con el numero directamente?

    # Metodos accesores

    def get_area_del_conocimiento(self):
        return self.__area_del_conocimiento

    def get_nro_libros_estante(self):
        return self.__nro_libros_estante
    
    def get_libros_estante(self):
        return self.__libros_estante

    # Metodos modificadores

    def set_area_del_conocimiento(self, nueva_area_del_conocimiento):
        self.area_del_conocimiento = nueva_area_del_conocimiento
    
    def set_nro_libros_estante(self):
        self.__nro_libros_estante += 1
        
    def buscar_libro_estante(self, titulo, codigo_isbn):
        for indice, libro in enumerate(self.__nro_libros_estante):
            if indice >= self.__nro_libros_estante:
                break
            if libro is not None:
                if libro.get_titulo() == titulo or libro.get_codigo_isbn() == codigo_isbn:
                    return indice, libro
        return -1, None
    
    def eliminar_libro_estante(self, titulo, codigo_isbn):
        indice, libro = self.buscar_libro_estante(titulo, codigo_isbn)
        if indice != -1:
            for libro in range(indice, self.__nro_libros_estante, 1):
                self.__libros_estante[libro] = self.__libros_estante[libro+1]
            self.__libros_estante[libro+1] = None
            self.__nro_libros_estante -= 1