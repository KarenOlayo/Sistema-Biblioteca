from Persona import Persona

class Bibliotecario(Persona):
    
    def __init__(self, nombre, apellido, fecha_nacimiento, identificacion, email):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__identificacion = identificacion
        self.__email = email

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