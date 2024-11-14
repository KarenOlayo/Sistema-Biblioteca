class Multa:
    
    def __init__(self, codigo, fecha_inicio, fecha_fin, estado):
        self.__codigo = codigo
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__lector = [] #se almacena en una lista?

# Metodos Accesores y Modificadores

def get_codigo(self):
    return self.__codigo

def get_fecha_inicio(self):
    return self.__fecha_inicio

def get_fecha_fin(self):
    return self.__fecha_fin

def get_lector(self):
    return self.__lector

def set_fecha_inicio(self, nueva_fecha_inicio):
    self.__fecha_inicio= nueva_fecha_inicio

def set_fecha_fin(self, nueva_fecha_fin):
    self.__fecha_fin = nueva_fecha_fin

def calcular_multa(self):
    pass

def mostrar_resumen_multa(self):
    pass

def mostrar_estado_multa(self):
    pass