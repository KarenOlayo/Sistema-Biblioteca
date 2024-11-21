from Persona import Persona
import datetime
from email_validator import validate_email, EmailNotValidError

class Bibliotecario(Persona):
    
    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Bibliotecario a partir de un diccionario.

        Args:
            data (dict): Diccionario con los datos del bibliotecario.
        Returns:
            Lector: Instancia de Lector creada.
            """
            
        try:
            # Validar y procesar los datos
            nombre = data['nombre']
            apellido = data['apellido']
            
            # Convertir fecha de nacimiento de string a datetime
            fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], '%d/%m/%Y')
            
            identificacion = data['identificacion']
            
            # Validar el correo electrónico
            email = data['email']
            validacion = validate_email(email)
            email = validacion.email  # Normaliza el correo electrónico
            
            # Crear y devolver la instancia de Bibliotecario
            return cls(nombre, apellido, fecha_nacimiento, identificacion, email)

        except KeyError as e:
            raise ValueError(f"Falta el campo obligatorio: {e}")
        except ValueError as e:
            raise ValueError(f"Error en los datos: {e}")

    def __init__(self, nombre, apellido, fecha_nacimiento, identificacion, email):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__identificacion = identificacion
        self.__email = email
        
        # validacion del correo
        try:
            validacion = validate_email(email)
            self.__email = validacion.email  # se guarda el correo validado y normalizado
        except EmailNotValidError as e:
            raise ValueError(f"Correo no válido: {e}")
    
    def to_dict(self):
        return {
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'fecha_nacimiento': self.__fecha_nacimiento.strftime('%d/%m/%Y'),
            'identificacion': self.__identificacion,
            'email': self.__email
        }

    # Metodos Accesores

    def get_identificacion(self):
        return self.__identificacion

    def get_email(self):
        return self.__email

    # Metodos  Modificadores

    def set_identificacion(self, nueva_identificacion):
        self.__identificacion = nueva_identificacion

    def  set_email(self, nuevo_email):
        self.__email = nuevo_email