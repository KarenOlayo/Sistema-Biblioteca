from Persona import Persona
import datetime
from email_validator import validate_email, EmailNotValidError

class Bibliotecario(Persona):
    
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