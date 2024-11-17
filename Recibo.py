from DataInicial import TIPOS_DE_RECIBOS

class Recibo:
    
    def __init__(self, nombre_biblioteca, codigo_recibo, fecha, identificacion_lector,tipo, informacion):
        
        self.__nombre_biblioteca = nombre_biblioteca
        self.__codigo_recibo = codigo_recibo
        self.__fecha = fecha
        self.__identificacion_lector = identificacion_lector
        self.__informacion = informacion
        
        if tipo in TIPOS_DE_RECIBOS:
            self.__tipo = tipo
        else:
            print(f"El tipo de recibo {tipo} es invalido.")
                
    # Metodos Accesores y Modificadores

    def get_tipo(self):
        return self.__tipo
        
    def set_tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    def __repr__(self):
        return f"""---
Biblioteca: {self.__nombre_biblioteca}
Recibo N° {self.__codigo_recibo}
Fecha: {self.__fecha}
Identificación del lector: {self.__identificacion_lector}
Proceso: {self.__tipo}
Resumen:
{self.__informacion}
---
"""