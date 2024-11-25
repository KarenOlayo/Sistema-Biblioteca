import numpy as np
from Persona import Persona
import datetime
from email_validator import validate_email, EmailNotValidError

class Lector(Persona):
    
    def  __init__(self, nombre:str, apellido:str, fecha_nacimiento:datetime.date, identificacion:str, email:str):
        
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__identificacion = identificacion
        
        try:
            validacion = validate_email(email)
            self.__email = validacion.email  # se guarda el correo validado y normalizado
        except EmailNotValidError as e:
            raise ValueError(f"Correo no válido: {e}")
        
        self.__prestamos = [] #instancias de Prestamo , funciona como un historial
        self.__recibos = []
        
        self.__prestamos_vigentes = np.full((3),fill_value=None, dtype=object) #instancias de Libro
        self.__nro_prestamos_vigentes = 0
        
        self.__multas = np.full((3),fill_value=None, dtype=object)
        self.__nro_multas = 0
                
        
    # Metodos Accesores

    def get_identificacion(self):
        return self.__identificacion
    
    def get_email(self):
        return self.__email

    def get_prestamos_vigentes(self):
        return self.__prestamos_vigentes
    
    def get_prestamos(self):
        return self.__prestamos
    
    def get_multas(self):
        return self.__multas

    def get_recibos(self):
        return self.__recibos
    
    def get_nro_multas(self):
        return self.__nro_multas
    
    def get_nro_prestamos_vigentes(self):
        return self.__nro_prestamos_vigentes
    
    def get_codigo_multas_vigentes(self):
        
        nro_multas_vigentes = self.consultar_nro_multas_vigentes() # retorna un int
            
        if nro_multas_vigentes > 0:
            codigos_multas_vigentes = []
            for i in range(self.__nro_multas):
                if self.__multas[i] is not None:
                    codigo = f"'{self.__multas[i].get_codigo()}'"
                    codigos_multas_vigentes.append(codigo)
            return codigos_multas_vigentes
        else:
            return f"No."

    # Metodos  Modificadores

    def set_identificacion(self, nueva_identificacion):
        self.__identificacion = nueva_identificacion

    def  set_email(self, nuevo_email):
        self.__email = nuevo_email
    
    def aumentar_nro_multas(self):
        self.__nro_multas += 1
        
    # Metodos de búsqueda
    
    def buscar_prestamo(self, codigo_prestamo):
        for prestamo in self.__prestamos :
            if prestamo.get_codigo() == codigo_prestamo:
                return prestamo # retorna un objeto
        return None
    
    def buscar_multa(self, codigo_multa):
        
        for i in range(self.__nro_multas):
            if self.__multas[i] is not None and self.__multas[i].get_codigo() == codigo_multa:
                return i
        return -1
    
    def buscar_recibo(self, codigo_recibo):
        for recibo in self.__recibos:
            if recibo.get_codigo() == codigo_recibo:
                return recibo # retorna un objeto
        return None
    
    # Metodos para agregar y guaradr
    
    def agregar_libro_a_prestamos_vigentes(self,libro:object):
        if self.__nro_prestamos_vigentes < 3:
            self.__prestamos_vigentes[self.__nro_prestamos_vigentes] = libro
            self.__nro_prestamos_vigentes += 1
    
    def guardar_multa(self, multa:object):
        if self.__nro_multas < 3:
            if multa is not None:
                self.__multas[self.__nro_multas] = multa
                self.__nro_multas += 1
    
    def guardar_recibo(self, recibo:object):
        if recibo is not None:
            codigo_recibo = recibo.get_codigo()
            if self.buscar_recibo(codigo_recibo) is None:
                self.__recibos.append(recibo)
        else:
            print("No se generó un recibo. No se pudo guardar en la lista del lector.")
    
    def guardar_prestamo(self, prestamo:object):
        codigo_prestamo = prestamo.get_codigo()
        if self.buscar_prestamo(codigo_prestamo) is None:
            self.__prestamos.append(prestamo)
    
    # Otros metodos
    
    def consultar_nro_multas_vigentes(self):
        
        nro_multas_vigentes = 0
        for multa in self.__multas:
            if multa is not None and multa.get_estado() == "Vigente":
                nro_multas_vigentes +=1
        return nro_multas_vigentes

    def verificar_requisitos_prestamo(self):
        self.resetear_multas()
        nro_multas_vigentes = self.consultar_nro_multas_vigentes()
        if nro_multas_vigentes == 0:
            if self.__nro_multas < 3:
                if self.__nro_prestamos_vigentes < 3:
                    return True
        return False
    
    def verificar_requisitos_renovacion(self, codigo_prestamo):
        
        cumple_requisitos = self.verificar_requisitos_prestamo() # Devuelve True o False
        
        if cumple_requisitos is True:
            prestamo = self.buscar_prestamo(codigo_prestamo)
            
            if prestamo is not None:
                lector_del_prestamo = prestamo.get_lector().get_identificacion()
                
                if lector_del_prestamo == self.__identificacion:
                    if prestamo.get_nro_renovaciones() < 2 :
                        return True
        return False

    def eliminar_libro_de_prestamos_vigentes(self, libro:object):
        titulo = libro.get_titulo()
        codigo_isbn = libro.get_codigo_isbn()
        
        for i in range(self.__nro_prestamos_vigentes):
            libro_prestado = self.__prestamos_vigentes[i]
            if libro_prestado is not None and libro_prestado.get_titulo() == titulo and libro_prestado.get_codigo_isbn() == codigo_isbn:
                for j in range(i, self.__nro_prestamos_vigentes - 1):
                    self.__prestamos_vigentes[j] = self.__prestamos_vigentes[j+1]
                self.__prestamos_vigentes[self.__nro_prestamos_vigentes-1] = None
                self.__nro_prestamos_vigentes -= 1
                
    def resetear_multas(self):
        
        # Verificar si hay exactamente 3 multas y todas están en estado "Terminado"
        if self.__nro_multas == 3 and all(multa is not None and multa.get_estado() == "Terminado" for multa in self.__multas):                            
            # Eliminar todas las multas
            self.__multas = np.full((3), fill_value=None, dtype=object)
            self.__nro_multas = 0
    
    # Metodo de representacion
    
    def __repr__(self):
        return f"""
Identificación: '{self.__identificacion}'
Apellido: '{self.get_apellido()}'
Nombre: '{self.get_nombre()}'
Fecha de Nacimiento: '{self.get_fecha_nacimiento()}'
Correo Electrónico: '{self.__email}'
No. Préstamos: '{len(self.__prestamos)}'
No. Préstamos Vigentes: '{self.__nro_prestamos_vigentes}'
No. Multas: '{self.__nro_multas}'
Multa(s) Vigente(s): {print(self.get_codigo_multas_vigentes())}
"""