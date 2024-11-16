from DataInicial import ESTADO_PRESTAMO
from Libro import Libro
from datetime import datetime , timedelta

class Prestamo:
    from Lector import Lector
    def __init__(self, codigo, lector:Lector, libro:Libro, fecha_prestamo:datetime, fecha_devolucion:datetime=None, fecha_entrega:str='',estado:str='Vigente'):
        self.__codigo = codigo
        self.__lector = lector
        self.__libro = libro
        self.__fecha_prestamo = datetime.strptime(fecha_prestamo, '%d/%m/%Y').date()
        self.__fecha_devolucion = datetime.strptime(fecha_prestamo, '%d/%m/%Y').date() + timedelta(days=30)
        
        if fecha_entrega is not '':
            self.__fecha_entrega = datetime.strptime(fecha_entrega, '%d/%m/%Y').date()
            
        self.__nro_renovaciones = 0
        self.__estado = estado if estado in ESTADO_PRESTAMO else 'Vigente'
        self.actualizar_estado()
        
    def actualizar_estado(self):
        
        hoy = datetime.today().date()
        
        if hoy > self.__fecha_devolucion :
            estado = "Atrasado"
            self.__estado = estado
        elif self.__fecha_entrega is not None:
            estado = "Terminado"
            self.__estado = estado
        else:
            estado = "Vigente"
            self.__estado = estado

    # Metodos accesores
    
    def get_codigo(self):
        return self.__codigo
    
    def get_lector(self):
        return self.__lector
    
    def get_libro(self):
        return self.__libro
    
    def get_fecha_prestamo(self):
        return self.__fecha_prestamo
    
    def get_fecha_devolucion(self):
        return self.__fecha_devolucion
    
    def get_fecha_entrega(self):
        
        return self.__fecha_entrega
    
    def get_estado_prestamo(self):
        self.actualizar_estado()
        return self.__estado
    
    def get_nro_renovaciones(self):
        return self.__nro_renovaciones
    
    # Metodos modificadores
    
    def set_fecha_devolucion(self, nueva_fecha_devolucion):
        self.__fecha_devolucion = nueva_fecha_devolucion
    
    def set_fecha_entrega(self, fecha_entrega):
        self.__fecha_entrega = datetime.strptime(fecha_entrega, '%d/%m/%Y').date() 
           
    def incrementar_nro_renovaciones(self):
        self.__nro_renovaciones += 1
        
    # Metodo repr
    
    def __repr__(self):
        return f"Codigo Prestamo: {self.__codigo}"