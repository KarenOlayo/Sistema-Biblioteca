from DataInicial import TIPOS_DE_RECIBOS
from datetime import datetime

class Recibo:

    @staticmethod
    def from_dict(data, lectores):
        """
        Crea una instancia de Recibo a partir de un diccionario.

        Args:
            data (dict): Diccionario con los datos del recibo.
            lectores (list): Lista de objetos Lector ya cargados.

        Returns:
            Recibo: Instancia de Recibo creada.
        """
        nombre_biblioteca = data['nombre_biblioteca']
        codigo = data['codigo_recibo']
        tipo = data['proceso']
        fecha = datetime.strptime(data['fecha'], "%d/%m/%Y")
        informacion = data['informacion']
        
        # Buscar el lector asociado por identificación
        lector = next((l for l in lectores if l.get_identificacion() == data['identificacion_lector']), None)
        if lector is None:
            print(f"No se encontró el lector con identificación {data['identificacion_lector']}")

        # Crear y retornar el objeto Recibo
        return Recibo(
            nombre_biblioteca=nombre_biblioteca,
            codigo=codigo,
            tipo=tipo,
            fecha=fecha,
            lector=lector,
            informacion=informacion
        )

    
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
    
    def to_dict(self):
        return {
            'nombre_biblioteca': self.__nombre_biblioteca,
            'fecha': self.__fecha.strftime("%d/%m/%Y"),
            'codigo_recibo': self.__codigo,
            'proceso': self.__tipo,
            'identificacion_lector': self.__lector.get_identificacion(),
            'informacion': self.__informacion
        }
        
    def get_codigo(self):
        return self.__codigo
    
    def get_informacion(self):
        return self.__informacion
    
    def __repr__(self):
        return f"""Biblioteca: {self.__nombre_biblioteca}
Recibo N° {self.__codigo}
Fecha: {self.__fecha}
Identificación del lector: {self.__lector.get_identificacion()}
Proceso: {self.__tipo}
Resumen:
{self.__informacion}
"""