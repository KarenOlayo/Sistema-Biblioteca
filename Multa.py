from datetime import datetime
from Prestamo import Prestamo
from Lector import Lector

class Multa:
        
    def __init__(self, codigo=str, prestamo=Prestamo, lector=Lector , dias_penalizacion=int , fecha_inicio:datetime=None, fecha_fin:datetime=None, estado:str='Vigente'):
        
        self.__codigo = codigo
        self.__prestamo = prestamo
        self.__lector = lector
        self.__dias_penalizacion = dias_penalizacion
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__estado = estado
        self.actualizar_estado()

    # Metodos Accesores 
    
    def get_codigo(self):
        return self.__codigo
    
    def get_prestamo(self):
        return self.__prestamo
    
    def get_lector(self):
        return self.__lector
    
    def get_dias_penalizacion(self):
        return self.__dias_penalizacion

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def get_fecha_fin(self):
        return self.__fecha_fin
    
    def get_estado(self):
        return self.__estado

    
    # metodo repr
    
    def __repr__(self):
        return f"""Codigo Multa: {self.__codigo}
Codigo Prestamo: {self.__prestamo.get_codigo()}
Identificación Lector: {self.__lector.get_identificacion()}
Dias Penalización: {self.__dias_penalizacion}
Fecha Inicio: {self.__fecha_inicio}
Fecha Fin: {self.__fecha_fin}
Estado Multa: {self.__estado}"""
    
    # metodo funcional
    
    def actualizar_estado(self):
        pass
    