import numpy as np
from Estante import Estante
from Autor import Autor
from Lector import Lector
"""Hola gente"""
class Biblioteca:
    
    def __init__(self, nombre, ubicacion, horario_atencion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__horario_atencion = horario_atencion
        self.__bibliotecario = []
        self.__estantes = np.full((5), fill_value=None, dtype=object)
        self.__numero_estantes = 0
        self.__autores = []
        self.__lectores = []
        self.__recibos = []

#¿se almacena la informacion del bibliotecario en una lista?

# Metodos Accesores

def get_nombre(self):
    return self.__nombre

def get_ubicacion(self):
    return self.__ubicacion

def  get_horario_atencion(self):
    return self.__horario_atencion

# Metodos  Modificadores

def set_nombre(self, nuevo_nombre):
    self.__nombre = nuevo_nombre

def set_ubicacion(self, nueva_ubicacion):
    self.__ubicacion = nueva_ubicacion

def  set_horario_atencion(self, nuevo_horario):
    self.__horario_atencion = nuevo_horario

def buscar_estante(self, area_del_conocimiento):
    for i in self.__estantes:
        if self.__estantes[i] is not None and self.__estantes[i].get_area_del_conocimiento() == area_del_conocimiento:
            return self.__estantes[i]
        else:
            return None

def agregar_estante(self, area_del_conocimiento):
    estante = Estante(self, area_del_conocimiento)
    
    if self.buscar_estante(area_del_conocimiento) == None: #no esta registrado
        self.__estantes.append(estante)

#¿crear el objeto antes o despues de validar que no esta registrado?

def buscar_autor(self, nombre, apellido):
    for i in self.__autores :
        if self.__autores[i].get_nombre() == nombre and self.__autores[i].get_apellido() == apellido:
            return self.__autores[i]
        else:
            return None
        
#las listas tienen posicion -1 ¿es correcto retornar un objeto?

def agregar_autor(self, nombre, apellido, fecha_nacimiento, pais_origen, fecha_fallecimiento=None):
    autor = Autor(self, nombre, apellido, fecha_nacimiento, pais_origen, fecha_fallecimiento)
    if self.__autores.buscar_autor(nombre, apellido) == None : #no esta registrado
        self.__autores.append(autor)

#¿crear el objeto antes o despues de validar que no esta registrado?

def buscar_lector(self, identificacion):
    for i in self.__lectores:
        if self.__lectores[i].get_identificacion() == identificacion:
            return self.__lectores[i]
        else:
            return None

def agregar_lector(self, nombre, apellido, fecha_nacimiento, identificacion, email):
    
    lector = Lector(self, nombre, apellido, fecha_nacimiento, identificacion, email)
    
    if self.__lectores.buscar_lector() == None :
        self.__lectores.append(lector)

#¿crear el objeto antes o despues de validar que no esta registrado?

def eliminar_lector(self, identificacion):
    pass