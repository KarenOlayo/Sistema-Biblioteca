from datetime import timedelta
from Prestamo import Prestamo

class Multa:
        
    def __init__(self, codigo=str, prestamo=Prestamo, lector=None ,fecha_inicio=None, fecha_fin=None, estado='Vigente'):
        
        self.__codigo = codigo
        self.__lector = lector
        self.__prestamo = prestamo
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin

    # Metodos Accesores y Modificadores

    def get_codigo(self):
        return self.__codigo

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def get_fecha_fin(self):
        return self.__fecha_fin

    def get_lector(self):
        lector = self.__prestamo.get_lector()
        return lector

    def set_fecha_inicio(self, nueva_fecha_inicio):
        self.__fecha_inicio= nueva_fecha_inicio

    def set_fecha_fin(self, nueva_fecha_fin):
        self.__fecha_fin = nueva_fecha_fin