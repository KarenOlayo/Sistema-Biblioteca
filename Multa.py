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
        self.actualizar_estado()
        return self.__estado

    # Metodos modificadores
    
    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado
    
    def actualizar_estado(self):
        hoy = datetime.today().date()
        if hoy > self.__fecha_fin:
            self.set_estado("Terminado")
    
    # metodo repr
    
    def __repr__(self):
        return f"""
Código Multa: {self.__codigo}
Código Prestamo: {self.__prestamo.get_codigo()}
Identificación Lector: {self.__lector.get_identificacion()}
Dias Penalización: {self.__dias_penalizacion}
Fecha Inicio: {self.__fecha_inicio}
Fecha Fin: {self.__fecha_fin}
Estado Multa: {self.__estado}"""
    
    