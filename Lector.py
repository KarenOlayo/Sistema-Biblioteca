import numpy as np
from Persona import Persona
from Libro import Libro
from Multa import Multa
import datetime
from email_validator import validate_email, EmailNotValidError

class Lector(Persona):
    
    def  __init__(self, nombre=str, apellido=str, fecha_nacimiento=datetime.date, identificacion=str, email=str):
        
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__identificacion = identificacion
        self.__email = email
        
        self.__prestamos = [] #objetos de la clase Prestamo , funciona como un historial
        
        self.__prestamos_vigentes = np.full((3),fill_value=None, dtype=Libro)
        self.__nro_prestamos_vigentes = 0
        
        self.__multas = np.full((3),fill_value=None, dtype=Multa)
        self.__nro_multas = 0
                
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
    
    def get_historial_prestamos(self):
        return self.__historial_prestamos

    def get_prestamos_vigentes(self):
        return self.__prestamos_vigentes
    
    def get_multas_vigentes(self):
        return self.__multas_vigentes
    
    def get_prestamos(self):
        return self.__prestamos
    
    def get_nro_multas(self):
        return self.__nro_multas

    # Metodos  Modificadores

    def set_identificacion(self, nueva_identificacion):
        self.__identificacion = nueva_identificacion

    def  set_email(self, nuevo_email):
        self.__email = nuevo_email
    
    def set_nro_multas(self):
        self.__nro_multas += 1
    
    # Metodos funcionales
    
    def buscar_prestamo(self, codigo_prestamo):
        for prestamo in self.__prestamos :
            if prestamo.get_codigo() == codigo_prestamo:
                return prestamo # retorna un objeto
            else:
                return None
    
    def consultar_existencia_multa_vigente(self):
        for multa in self.__multas:
            if multa is not None and multa.get_estado() == "Vigente":
                return multa
        return None

    def verificar_requisitos_prestamo(self):
        multa_vigente = self.consultar_existencia_multa_vigente()
        if multa_vigente is None:
            if self.__nro_multas < 3:
                if self.__nro_prestamos_vigentes < 3:
                    return True
        else:
            return False
    
    def verificar_requisitos_renovacion(self, codigo_prestamo):
        cumple_requisitos = self.verificar_requisitos_prestamo() # Devuelve True o False
        if cumple_requisitos is True:
            prestamo = self.buscar_prestamo(codigo_prestamo)
            if prestamo is not None:
                if prestamo.get_nro_renovaciones() < 2 :
                    return True
                else:
                    return False
    
    def agregar_libro_a_prestamos_vigentes(self,libro:Libro):
        if self.__nro_prestamos_vigentes < 3:
            self.__prestamos_vigentes[self.__nro_prestamos_vigentes] = libro
            self.__nro_prestamos_vigentes += 1

    def eliminar_libro_de_prestamos_vigentes(self, libro:Libro):
        titulo = libro.get_titulo()
        codigo_isbn = libro.get_codigo_isbn()
        
        for i in range(self.__nro_prestamos_vigentes):
            libro_prestado = self.__prestamos_vigentes[i]
            if libro_prestado is not None and libro_prestado.get_titulo() == titulo and libro_prestado.get_codigo_isbn() == codigo_isbn:
                for j in range(i, self.__nro_prestamos_vigentes - 1):
                    self.__prestamos_vigentes[j] = self.__prestamos_vigentes[j+1]
                self.__prestamos_vigentes[self.__nro_prestamos_vigentes-1] = None
                self.__nro_prestamos_vigentes -= 1
                