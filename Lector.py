from Persona import Persona

class Lector(Persona):
    
    def  __init__(self, nombre, apellido, fecha_nacimiento, identificacion, email):
        
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__identificacion = identificacion
        self.__email = email
        self.__historial_prestamos = []
        self.__prestamos_vigentes = []
        self.__multas_vigentes = []
        self.__nro_multas = 0

    # Metodos Accesores

    def get_identificacion(self):
        return self.__identificacion
    
    def get_email(self):
        return self.__email
    
    def get_historial_prestamos(self):
        return self.__historial_prestamos

    def get_prestamos_vigentes(self):
        return self.__prestamos_vigentes
    
    def get_multas_vigentes(self):
        return self.__multas_vigentes
    
    def get_nro_multas(self):
        return self.__nro_multas

    # Metodos  Modificadores

    def set_identificacion(self, nueva_identificacion):
        self.__identificacion = nueva_identificacion

    def  set_email(self, nuevo_email):
        self.__email = nuevo_email
    
    def set_nro_multas(self):
        self.__nro_multas += 1
    
    # Metodo para verificar si el lector cumple con los requisitos para prestar un libro

    def verificar_requisitos_prestamo(self):
        if len(self.__multas_vigentes) == 0:
            if len(self.__prestamos_vigentes) < 3:
                if self.__nro_multas < 3:
                    return True
        else:
            return False