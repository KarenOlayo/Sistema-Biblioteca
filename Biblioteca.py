import numpy as np
from Estante import Estante
from Bibliotecario import Bibliotecario
from Lector import Lector
from Autor import Autor

class Biblioteca:
    
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__estantes = np.full((5), fill_value=None, dtype=object)
        self.__nro_estantes = 0
        self.__bibliotecarios = []
        self.__lectores = []
        self.__autores = []
        self.__multas = []
        self.__recibos = []

    # Metodos Accesores

    def get_nombre(self):
        return self.__nombre

    def get_ubicacion(self):
        return self.__ubicacion

    def  get_horario_atencion(self):
        return self.__horario_atencion
    
    def get_estantes(self):
        return self.__estantes
    
    def get_nro_estantes(self):
        return self.__nro_estantes
    
    def get_bibliotecarios(self):
        return self.__bibliotecarios
    
    def get_lectores(self):
        return self.__lectores
    
    def get_autores(self):
        return self.__autores
    
    def get_multas(self):
        return self.__multas
    
    def get_recibos(self):
        return self.__recibos

    # Metodos  Modificadores

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_ubicacion(self, nueva_ubicacion):
        self.__ubicacion = nueva_ubicacion

    def  set_horario_atencion(self, nuevo_horario):
        self.__horario_atencion = nuevo_horario

    # Metodos de busqueda

    def buscar_estante(self, area_del_conocimiento): 
        for indice, estante in enumerate(self.__estantes):
            if estante is not None and estante.get_area_del_conocimiento() == area_del_conocimiento:
                return indice , estante # retorna la posicion y el objeto
        return -1, None
    
    def buscar_bibliotecario(self, identificacion):
        for bibliotecario in self.__bibliotecarios:
            if bibliotecario.get_identificacion() == identificacion:
                return bibliotecario # retorna un objeto
        return None
    
    def buscar_lector(self, identificacion):
        for lector in self.__lectores:
            if lector.get_identificacion() == identificacion:
                return lector # retorna un objeto
        return None

    def buscar_autor(self, nombre, apellido):
        for autor in self.__autores :
            if autor.get_nombre() == nombre and autor.get_apellido() == apellido:
                return autor # retorna un objeto
        return None
    
    def buscar_multa(self, codigo_multa):
        for multa in self.__multas:
            if multa.get_codigo() == codigo_multa:
                return multa
            else:
                return None
            
    # Metodos de agregacion

    def agregar_estante(self, area_del_conocimiento):
        _, estante = self.buscar_estante(area_del_conocimiento)
        if estante is None:
            if self.__nro_estantes < len(self.__estantes):
                estante = Estante(area_del_conocimiento)
                self.__estantes[self.__nro_estantes] = estante
                self.__nro_estantes += 1
    
    def agregar_bibliotecario(self, nombre, apellido, fecha_nacimiento, identificacion, email):
        if self.buscar_bibliotecario(identificacion) == None:
            bibliotecario = Bibliotecario(nombre, apellido, fecha_nacimiento, identificacion, email)
            self.__bibliotecarios.append(bibliotecario)
            print(f"Bibliotecario {nombre} agregado con exito")

    def agregar_autor(self, nombre, apellido, fecha_nacimiento, fecha_fallecimiento, pais_origen):
        if self.buscar_autor(nombre, apellido) == None : 
            autor = Autor(nombre, apellido, fecha_nacimiento, fecha_fallecimiento, pais_origen)
            self.__autores.append(autor)

    def agregar_lector(self, nombre, apellido, fecha_nacimiento, identificacion, email):
        if self.buscar_lector(identificacion) == None :
            lector = Lector(nombre, apellido, fecha_nacimiento, identificacion, email)
            self.__lectores.append(lector)
            print(f"Lector {nombre} agregado.")

    # Metodos de eliminacion

    def eliminar_estante(self, area_del_conocimiento):
        indice , estante = self.buscar_estante(area_del_conocimiento)
        if estante is not None:
            self.__estantes[indice] = None
            self.__nro_estantes -= 1
    
    def eliminar_bibliotecario(self, identificacion):
        bibliotecario = self.buscar_bibliotecario(identificacion)
        if bibliotecario is not None:
            self.__bibliotecarios.remove(bibliotecario)
            
    def eliminar_lector(self, identificacion):
        lector = self.buscar_lector(identificacion)
        if lector is not None:
            self.__lectores.remove(lector)

    def eliminar_autor(self, nombre, apellido):
        autor = self.buscar_autor(nombre, apellido)
        if autor is not None:
            self.__autores.remove(autor)       
