import numpy as np

class Estante:
    
    AREAS_DEL_CONOCIMIENTO = [
        "Ciencias Sociales",
        "Ciencias Humanas",
        "Ciencias Exactas",
        "Ciencias Políticas",
        "Literatura"
    ]
    
    def __init__(self, area_del_conocimiento):
        
        if area_del_conocimiento in Estante.AREAS_DEL_CONOCIMIENTO:
                self.__area_del_conocimiento = area_del_conocimiento
        else:
                print(f"Área del conocimiento '{area_del_conocimiento}' no es válida.")
        
        self.__libros_estante = np.full((100), fill_value=None, dtype=object)
        self.__nro_libros_estante = 0
        self.__biblioteca_asignada = []
        
        #Preguntas: Como maximo, un estante tendra 100 libros ¿Se debera poner una variable con este valor,
        #para hacer la validacion a la hora de agregar un libro?
        #¿La biblioteca asignada se almacena en una lista? O simplemente se indica el nombre de la misma

# Metodos accesores

def get_area_del_conocimiento(self):
    return self.__area_del_conocimiento

def get_nro_libros_estante(self):
    return self.__nro_libros_estante

# Metodos modificadores

def set_area_del_conocimiento(self, nueva_area_del_conocimiento):
    self.area_del_conocimiento = nueva_area_del_conocimiento