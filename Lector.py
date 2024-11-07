from Persona import Persona

class Lector(Persona):
    
    def  __init__(self, nombre, apellido, fecha_nacimiento, identificacion, email):
        
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__identificacion = identificacion
        self.__email = email
        self.__historial_prestamos = []
        self.__prestamos_vigentes = []
        self.__reservas_vigentes = []
        self.__multas_vigentes = []
        self.__multas_totales = 0

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