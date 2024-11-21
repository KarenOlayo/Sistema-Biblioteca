from Persona import Persona
from country_list import countries_for_language
from datetime import datetime

class Autor(Persona):
    
    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Autor a partir de un diccionario.
        
        Args:
            data (dict): Diccionario con los datos del autor.
        Returns:
            Autor: Instancia de Autor creada.
        """
        try:
            # Extraer y procesar los datos
            nombre = data['nombre']
            apellido = data['apellido']
            
            # Convertir fechas de string a datetime
            fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], '%d/%m/%Y')
            
            fecha_fallecimiento = (
                datetime.strptime(data['fecha_fallecimiento'], '%d/%m/%Y')
                if data.get('fecha_fallecimiento') else None
            )
            
            pais_origen = data.get('pais_origen', None)
            
            # Validar país de origen
            if pais_origen and pais_origen not in cls.PAISES:
                print(f"El país de origen '{pais_origen}' no es válido.")
            
            # Crear y devolver la instancia de Autor
            return cls(nombre, apellido, fecha_nacimiento, fecha_fallecimiento, pais_origen)

        except KeyError as e:
            raise ValueError(f"Falta el campo obligatorio: {e}")
        except ValueError as e:
            raise ValueError(f"Error en los datos: {e}")
    
    PAISES = dict(countries_for_language('es')).values()
    
    def __init__(self, nombre=str, apellido=str, fecha_nacimiento=datetime.date, fecha_fallecimiento=datetime.date, pais_origen:str=None):
        
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__fecha_fallecimiento = fecha_fallecimiento
        self.__obras_literarias =  []
        
        if pais_origen in Autor.PAISES:
            self.__pais_origen = pais_origen
        else:
            print(f"El pais de origen {pais_origen} no es válido.")
    
    def to_dict(self):
        return {
            'nombre': self.get_nombre(),
            'apellido': self.get_apellido(),
            'fecha_nacimiento': self.get_fecha_nacimiento() if self.get_fecha_nacimiento is not None else None,
            'fecha_fallecimiento': self.__fecha_fallecimiento if self.__fecha_fallecimiento is not None else None,
            'pais_origen': self.__pais_origen 
        }

    # Metodos Accesores
        
    def get_pais_origen(self):
        return self.__pais_origen
        
    def get_fecha_fallecimiento(self):
        return self.__fecha_fallecimiento

    def get_obras_literarias(self):
        return self.__obras_literarias
    
    def get_nombre_completo(self):
        return f"{self.get_nombre()} {self.get_apellido()}"

    # Metodos Modificadores
        
    def set_fecha_fallecimiento(self, fecha_fallecimiento):
        self.__fecha_fallecimiento = fecha_fallecimiento
        
    def set_pais_origen(self, nuevo_pais_origen):
        self.__pais_origen = nuevo_pais_origen
        
    # metodo de representacion
    
    def __repr__(self):
        return f"{self.get_nombre()} {self.get_apellido()}'"