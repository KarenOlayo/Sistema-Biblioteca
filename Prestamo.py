from DataInicial import ESTADO_PRESTAMO
from Libro import Libro
from Multa import Multa
from Biblioteca import Biblioteca
from datetime import datetime , timedelta

class Prestamo:
    from Lector import Lector
    def __init__(self, codigo, lector:Lector, libro:Libro, fecha_prestamo:datetime, fecha_devolucion:datetime=None, fecha_entrega:datetime='',estado:str='Vigente', biblioteca=Biblioteca):
        self.__codigo = codigo
        self.__lector = lector
        self.__libro = libro
        self.__biblioteca = biblioteca
        self.__fecha_prestamo = datetime.strptime(fecha_prestamo, '%d/%m/%Y').date()
        self.__fecha_devolucion = datetime.strptime(fecha_prestamo, '%d/%m/%Y').date() + timedelta(days=30)
        self.__fecha_entrega = fecha_entrega
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
    
    def calcular_fecha_devolucion(self):
        self.__fecha_devolucion = self.__fecha_prestamo + timedelta(days=30)
    
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
        self.calcular_fecha_devolucion()
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
    
    def incrementar_nro_renovaciones(self):
        self.__nro_renovaciones += 1
    
    # Metodos funcionales
    
    def calcular_dias_retraso(self):
        dias_retraso = (self.__fecha_entrega - self.__fecha_devolucion)/timedelta(days=1)
        return dias_retraso
    
    def calcular_multa(self):
        dias_retraso = self.calcular_dias_retraso()
        if dias_retraso > 0:
            dias_penalizacion = dias_retraso*2        
            codigo_multa = f"M{self.__biblioteca.get_nro_multas_bibliotecas()}"
            fecha_inicio = self.__fecha_entrega
            fecha_fin = self.__fecha_entrega + timedelta(days=dias_penalizacion)
            
            multa = Multa(codigo_multa,fecha_inicio, fecha_fin)
            self.__biblioteca.agregar_multa(multa)
            
            return multa #retornar dentro del condicional?
            