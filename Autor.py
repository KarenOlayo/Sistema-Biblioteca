from Persona import Persona
from country_list import countries_for_language
from datetime import datetime

class Autor(Persona):
    
    PAISES = dict(countries_for_language('es')).values()
    
    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:datetime.date, fecha_fallecimiento:datetime.date=None, pais_origen:str=None):
        
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__fecha_fallecimiento = fecha_fallecimiento
        
        if pais_origen in Autor.PAISES:
            self.__pais_origen = pais_origen
        else:
            print(f"El pais de origen {pais_origen} no es válido.")
    
    # Metodos Accesores
        
    def get_pais_origen(self):
        return self.__pais_origen
        
    def get_fecha_fallecimiento(self):
        return self.__fecha_fallecimiento

    # Metodos Modificadores
        
    def set_fecha_fallecimiento(self, fecha_fallecimiento):
        self.__fecha_fallecimiento = fecha_fallecimiento
        
    def set_pais_origen(self, nuevo_pais_origen):
        self.__pais_origen = nuevo_pais_origen
        
    # metodo de representacion
    
    def __repr__(self):
        return f"""
Apellido: '{self.get_apellido()}'
Nombre: '{self.get_nombre()}'
Fecha de Nacimiento: '{self.get_fecha_nacimiento()}'
Fecha de Fallecimiento: '{self.__fecha_fallecimiento}'
País de Origen: '{self.__pais_origen}'
    """