from DataInicial import TIPOS_DE_RECIBOS
from datetime import datetime

class Recibo:

    def __init__(self, nombre_biblioteca, codigo, tipo, fecha=datetime, lector=object, informacion=str):
        
        self.__nombre_biblioteca = nombre_biblioteca
        self.__codigo = codigo
        self.__fecha = fecha
        self.__lector = lector
        self.__informacion = informacion
        
        
        if tipo in TIPOS_DE_RECIBOS:
            self.__tipo = tipo
        else:
            print(f"El tipo de recibo {tipo} es invalido.")
        
    def get_codigo(self):
        return self.__codigo
    
    def get_informacion(self):
        return self.__informacion
    
    def get_tipo(self):
        return self.__tipo
    
    def get_lector(self):
        return self.__lector
    
    def get_fecha(self):
        return self.__fecha
            
    def __repr__(self):
        return f"""Biblioteca: {self.__nombre_biblioteca}
Recibo N° {self.__codigo}
Fecha: {self.__fecha}
Identificación del lector: {self.__lector.get_identificacion()}
Proceso: {self.__tipo}
Resumen:
{self.__informacion}
"""