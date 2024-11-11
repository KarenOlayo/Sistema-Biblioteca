class Persona:
    
    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
    
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido
        
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    # Metodos Modificadores

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    def set_apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido
        
    def set_fecha_nacimiento(self, nueva_fecha_nacimiento):
        self.__fecha_nacimiento = nueva_fecha_nacimiento

