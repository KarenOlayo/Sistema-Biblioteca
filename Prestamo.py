from DataInicial import ESTADO_PRESTAMO
from Libro import Libro
from Lector import Lector
from datetime import datetime , timedelta

class Prestamo:

    def __init__(self, codigo, lector:Lector, libro:Libro, fecha_prestamo:datetime, fecha_devolucion:datetime=None, fecha_entrega:datetime=None, dias_duracion:str=None, estado:str='Vigente', multa:object=None):
        self.__codigo = codigo
        self.__lector = lector
        self.__libro = libro
        self.__fecha_prestamo = datetime.strptime(fecha_prestamo, '%d-%m-%Y').date()
        self.__fecha_devolucion = datetime.strptime(fecha_prestamo, '%d-%m-%Y').date() + timedelta(days=30)
        self.__fecha_entrega = None 
        self.__dias_duracion = None
        self.calcular_dias_duracion()
        self.__estado = estado if estado in ESTADO_PRESTAMO else 'Vigente'
        self.__multa = None
        self.__nro_renovaciones = 0

    def actualizar_estado(self):
        
        # Por defecto, es tado de un prestamo es "Vigente"
        # El estado "Terminado" se actualiza cuando se devuelve el libro
        # El estado "Renovado" se actualiza cuando se renueva el prestamo de un libro
        
        hoy = datetime.today().date()
        
        if hoy > self.__fecha_devolucion and self.__fecha_entrega is None:
            self.__estado = "Atrasado"
            
    def calcular_dias_duracion(self):
        if self.__fecha_entrega is not None:
            if self.__fecha_entrega >= self.__fecha_prestamo:
                self.__dias_duracion = (self.__fecha_entrega - self.__fecha_prestamo).days
                return self.__dias_duracion
        return None
    
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
    
    def get_dias_duracion(self):
        return self.calcular_dias_duracion()
    
    def get_estado(self):
        self.actualizar_estado()
        return self.__estado
    
    def get_multa(self):
        return self.__multa
    
    def get_nro_renovaciones(self):
        return self.__nro_renovaciones
    
    # Metodos modificadores
    
    def set_fecha_devolucion(self, nueva_fecha_devolucion):
        self.__fecha_devolucion = datetime.strptime(nueva_fecha_devolucion, '%d-%m-%Y').date()
    
    def set_fecha_entrega(self, fecha_entrega):
        self.__fecha_entrega = datetime.strptime(fecha_entrega, '%d-%m-%Y').date()
    
    def set_multa(self, multa:object):
        from Multa import Multa
        if isinstance(multa, Multa):
            if self.__multa is None:
                self.__multa = multa
    
    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado
           
    def incrementar_nro_renovaciones(self):
        self.__nro_renovaciones += 1    
    
    def comprobar_multa_asignada(self): #comprobar existencia multa
        if self.__multa is not None:
            codigo = self.__multa.get_codigo()
            dias_penalizacion = self.__multa.get_dias_penalizacion()
            fecha_inicio = self.__multa.get_fecha_inicio()
            fecha_fin = self.__multa.get_fecha_fin()
            return f"""Si.
Codigo Multa: {codigo}.
Dias de Penalizacion: {int(dias_penalizacion)} dias.
Fecha Inicio: {fecha_inicio}
Fecha Fin: {fecha_fin}
"""
        return "No"
    
    def get_codigo_multa_asignada(self):
        if self.__multa is not None:
            return self.__multa.get_codigo()
        return "No."
        
    # Metodo repr
    
    def __repr__(self):
        return f"""
Código: '{self.__codigo}'
Identificación Lector: '{self.__lector.get_identificacion()}'
Titulo Libro: '{self.__libro.get_titulo()}'
Código ISBN: '{self.__libro.get_codigo_isbn()}'
Estado: '{self.__estado}'
Fecha Préstamo: '{self.__fecha_prestamo}'
Fecha Devolución: '{self.__fecha_devolucion}'
Fecha Entrega: '{self.__fecha_entrega}'
Duración: '{self.__dias_duracion} días.'
Estado: '{self.__estado}'
Multa: '{self.get_codigo_multa_asignada()}'
"""