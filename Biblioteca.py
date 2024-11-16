import numpy as np
from datetime import timedelta
from Estante import Estante
from Bibliotecario import Bibliotecario
from Lector import Lector
from Autor import Autor
from Prestamo import Prestamo
from Multa import Multa
from Recibo import Recibo

class Biblioteca:
    
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        
        self.__estantes = np.full((5), fill_value=None, dtype=Estante)
        self.__nro_estantes = 0
        
        self.__bibliotecarios = []
        self.__lectores = []
        self.__autores = []
        
        self.__recibos = []
        self.__nro_recibos = 0
        
        self.__multas = []
        self.__nro_multas_biblioteca = 1
        
        self.__prestamos = []
        self.__nro_prestamos_biblioteca = 1

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
    
    def get_nro_multas_bibliotecas(self):
        return self.__nro_multas_biblioteca
    
    def get_nro_prestamos_biblioteca(self):
        return self.__nro_prestamos_biblioteca

    # Metodos  Modificadores

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_ubicacion(self, nueva_ubicacion):
        self.__ubicacion = nueva_ubicacion

    def set_horario_atencion(self, nuevo_horario):
        self.__horario_atencion = nuevo_horario
    
    def agregar_multa(self, multa):
        self.__multas.append(multa)
        self.__nro_multas_biblioteca += 1

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
    def buscar_prestamo(self, codigo_prestamo):
        for prestamo in self.__prestamos:
            if prestamo.get_codigo() == codigo_prestamo:
                return prestamo
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
    
    def agregar_prestamo(self, prestamo=Prestamo):
        self.__prestamos.append(prestamo)
    
    def agregar_multa(self, multa=Multa):
        self.__multas.append(multa)
    
    # Sobre las multas
    
    def calcular_dias_retraso(self, prestamo=Prestamo):
        fecha_devolucion = prestamo.get_fecha_devolucion()
        fecha_entrega_libro = prestamo.get_fecha_entrega()
        dias_retraso = (fecha_entrega_libro - fecha_devolucion)/timedelta(days=1)
        return dias_retraso
    
    def calcular_multa(self, prestamo=Prestamo):
        dias_retraso = self.calcular_dias_retraso(prestamo)
        if dias_retraso > 0:
            dias_penalizacion = dias_retraso*2        
            codigo_multa = f"M{self.__nro_multas_bibliotecas()}"
            fecha_inicio = self.__fecha_entrega
            fecha_fin = self.__fecha_entrega + timedelta(days=dias_penalizacion)
            
            multa = Multa(codigo_multa,fecha_inicio, fecha_fin)
            self.agregar_multa(multa) # se agrega la multa a la lista de la biblioteca
            self.__nro_multas_biblioteca += 1
            
            lector = prestamo.get_lector()
            lector.agregar_multa(multa) # agrega la multa a las multas del letor
            
            return multa
    
    # sobre los recibos
    
    def generar_recibo(self, objeto=object, identificacion_lector=str):
        nombre_biblioteca = self.__nombre
        codigo_recibo = f"R{self.__nro_recibos+1}"
        
        if isinstance(objeto, Prestamo):
            fecha = objeto.get_fecha_prestamo()
    
            informacion = f"""Identificacion Lector = {objeto.get_lector().get_identificacion()}
            Titulo Libro: '{objeto.get_libro().get_titulo()}'\n
            Codigo ISBN: {objeto.get_libro().get_codigo_isbn()}\n
            Fecha Préstamo: {objeto.get_fecha_prestamo()}
            Fecha Devolución: {objeto.get_fecha_devolucion()}
            Codigo Préstamo: {objeto.get_codigo()}\n
            """
            recibo = Recibo(nombre_biblioteca, codigo_recibo, fecha,"Prestamo de Libro", informacion)
            
        elif isinstance(objeto, Multa):
            fecha = objeto.get_fecha_inicio()
            informacion = f"""Identificación Lector: {identificacion_lector}
            Codigo Multa: {objeto.get_codigo()}
            Fecha Inicio: {objeto.get_fecha_inicio()}
            Fecha Fin: {objeto.get_fecha_fin()}
            """
            recibo = Recibo(nombre_biblioteca,codigo_recibo, fecha,"Multa", informacion)
            
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