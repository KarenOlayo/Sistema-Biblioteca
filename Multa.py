from datetime import datetime
from Prestamo import Prestamo
from Lector import Lector

class Multa:
    
    class Multa:

        @staticmethod
        def from_dict(data, prestamos, lectores):
            """
            Crea una instancia de Multa a partir de un diccionario.

            Args:
                data (dict): Diccionario con los datos de la multa.
                prestamos (list): Lista de objetos Prestamo ya cargados.
                lectores (list): Lista de objetos Lector ya cargados.

            Returns:
                Multa: Instancia de Multa creada.
            """
            codigo = data['codigo_multa']
            
            # Buscar el prestamo asociado por código
            prestamo = next((p for p in prestamos if p.get_codigo() == data['codigo_prestamo']), None)
            if prestamo is None:
                print(f"No se encontró el préstamo con código {data['codigo_prestamo']}")
            
            # Buscar el lector asociado por identificación
            lector = next((l for l in lectores if l.get_identificacion() == data['identificacion_lector']), None)
            if lector is None:
                print(f"No se encontró el lector con identificación {data['identificacion_lector']}")
            
            dias_penalizacion = int(data['dias_penalizacion'])
            fecha_inicio = datetime.strptime(data['fecha_inicio'], '%d/%m/%Y')
            fecha_fin = datetime.strptime(data['fecha_fin'], '%d/%m/%Y') 
            estado = data['estado']

            return Multa(
                codigo=codigo,
                prestamo=prestamo,
                lector=lector,
                dias_penalizacion=dias_penalizacion,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                estado=estado
            )
        
    def __init__(self, codigo=str, prestamo=Prestamo, lector=Lector , dias_penalizacion=int , fecha_inicio:datetime=None, fecha_fin:datetime=None, estado:str='Vigente'):
        
        self.__codigo = codigo
        self.__prestamo = prestamo
        self.__lector = lector
        self.__dias_penalizacion = dias_penalizacion
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__estado = estado
        self.actualizar_estado()
    
    def to_dict(self):
        return {
            'codigo_multa': self.__codigo,
            'codigo_prestamo': self.__prestamo.get_codigo(),
            'identificacion_lector': self.__lector.get_identificacion(),
            'dias_penalizacion': self.__dias_penalizacion,
            'fecha_inicio': self.__fecha_inicio.strftime('%d/%m/%Y'),
            'fecha_fin': self.__fecha_fin.strftime('%d/%m/%Y'),
            'estado': self.__estado
        }

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