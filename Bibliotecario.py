from Persona import Persona

class Bibliotecario(Persona):
    
    def __init__(self, nombre, apellido, fecha_nacimiento, identificacion, email, biblioteca_asignada):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__identificacion = identificacion
        self.__email = email
        self.__biblioteca_asignada = biblioteca_asignada

# Metodos Accesores

def get_identificacion(self):
    return self.__identificacion

def get_email(self):
    return self.__email

def biblioteca_asignada(self):
    return self.__biblioteca_asignada

# Metodos  Modificadores

def set_identificacion(self, nueva_identificacion):
    self.__identificacion = nueva_identificacion

def  set_email(self, nuevo_email):
    self.__email = nuevo_email

def  set_biblioteca_asignada(self, nueva_biblioteca_asignada):
    self.__biblioteca_asignada = nueva_biblioteca_asignada

