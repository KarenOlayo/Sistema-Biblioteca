from Persona import Persona
from country_list import countries_for_language

class Autor(Persona):
    
    PAISES = dict(countries_for_language('es')).values()
    
    def __init__(self, nombre, apellido, fecha_nacimiento, fecha_fallecimiento, pais_origen):
        
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__fecha_fallecimiento = fecha_fallecimiento
        self.__obras_literarias =  []
        
        if pais_origen in Autor.PAISES:
            self.__pais_origen = pais_origen
        else:
            print(f"El pais de origen {pais_origen} no es válido. Intente nuevamente.")

# Metodos Accesores
    
def get_fecha_fallecimiento(self):
    return self.__fecha_fallecimiento
    
def set_pais_origen(self):
    return self.__pais_origen
    
# Metodos Modificadores
    
def set_fecha_fallecimiento(self, fecha_fallecimiento):
    self.__fecha_fallecimiento = fecha_fallecimiento
    
def set_pais_origen(self, nuevo_pais_origen):
    self.__pais_origen = nuevo_pais_origen
