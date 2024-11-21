import yaml
import numpy as np
import os
import csv
from datetime import datetime , timedelta
from Estante import Estante
from Bibliotecario import Bibliotecario
from Lector import Lector
from Autor import Autor
from Prestamo import Prestamo
from Multa import Multa
from Recibo import Recibo
from Libro import Libro

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
        self.__nro_recibos_biblioteca = 0
        
        self.__multas = []
        self.__nro_multas_biblioteca = 0
        
        self.__prestamos = []
        self.__nro_prestamos_biblioteca = 0
    
    # sobre los archivos
    
    def crear_archivos(self):
        
        """Crea los archivos necesarios para la aplicación si no existen.
        Inicializa encabezados en los CSV y un objeto vacío en YAML."""
        
        # Diccionario de archivos con sus configuraciones iniciales
        archivos = {
            
        "libros.csv": ["titulo",
                       "codigo_isbn",
                       "autor",
                       "area_del_conocimiento",
                       "genero", "nro_paginas",
                       "fecha_publicacion",
                       "origen",
                       "estado"],
        
        "bibliotecarios.csv": ["nombre",
                               "apellido",
                               "fecha_nacimiento",
                               "identificacion",
                               "email"],
        
        "autores.csv": ["nombre",
                        "apellido",
                        "fecha_nacimiento",
                        "fecha_fallecimiento",
                        "pais_origen"],
        
        "prestamos.csv": ["codigo",
                          "identificacion_lector",
                          "titulo_libro",
                          "codigo_isbn",
                          "fecha_prestamo",
                          "fecha_devolucion",
                          "fecha_entrega",
                          "dias_duracion",
                          "estado",
                          "multa"],  
        
        "lectores.yaml": None,  # YAML no necesita encabezados
        "recibos.yaml": None, 
        "multas.yaml": None,
    }
        
        for archivo, encabezados in archivos.items():
            if not os.path.exists(archivo):
                #crear el archivo dependiendo de su tipo
                
                if archivo.endswith(".csv") and encabezados:
                    
                    # Inicializar un archivo CSV con encabezados
                    with open(archivo, "w", newline="", encoding='utf-8') as archivo_csv:
                        writer = csv.writer(archivo_csv)
                        writer.writerow(encabezados)
                    
                elif archivo.endswith(".yaml"):
                    
                    # Inicializar un archivo YAML con un objeto vacío
                    with open(archivo, "w", encoding='utf-8') as archivo_yaml:
                        yaml.dump({}, archivo_yaml)
                else:
                    # Crear archivos de texto plano vacíos
                    with open(archivo, "w", encoding='utf-8') as archivo_txt:
                        pass
                
    # Metodos Accesores

    def get_nombre(self):
        return self.__nombre

    def get_ubicacion(self):
        return self.__ubicacion
    
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
    
    def get_nro_recibos_biblioteca(self):
        return self.__nro_recibos_biblioteca
    
    def get_nro_multas_bibliotecas(self):
        return self.__nro_multas_biblioteca
    
    def get_nro_prestamos_biblioteca(self):
        return self.__nro_prestamos_biblioteca

    # Metodos  Modificadores

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_ubicacion(self, nueva_ubicacion):
        self.__ubicacion = nueva_ubicacion

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
    
    def buscar_recibo(self, codigo_recibo):
        for recibo in self.__recibos:
            if recibo.get_codigo() == codigo_recibo:
                return recibo
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
            self.guardar_bibliotecario_en_archivo(bibliotecario)
            print(f"Bibliotecario {nombre} agregado con exito")

    def agregar_autor(self, nombre, apellido, fecha_nacimiento, fecha_fallecimiento, pais_origen):
        if self.buscar_autor(nombre, apellido) == None : 
            autor = Autor(nombre, apellido, fecha_nacimiento, fecha_fallecimiento, pais_origen)
            self.__autores.append(autor)
            self.guardar_autor_en_archivo(autor)
            print(f"Autor {nombre} {apellido} agregado con exito")

    def agregar_lector(self, nombre, apellido, fecha_nacimiento, identificacion, email):
        if self.buscar_lector(identificacion) == None :
            lector = Lector(nombre, apellido, fecha_nacimiento, identificacion, email)
            self.__lectores.append(lector)
            self.guardar_lector_en_archivo(lector)
            print(f"Lector {nombre} agregado.")
    
    # metodos para guardar
    
    def guardar_prestamo(self, prestamo=Prestamo):
        codigo_prestamo = prestamo.get_codigo()
        if self.buscar_prestamo(codigo_prestamo) is None:
            self.__prestamos.append(prestamo)
    
    def guardar_multa(self, multa=Multa):
        codigo_multa = multa.get_codigo()
        if self.buscar_multa(codigo_multa) is None:
            self.__multas.append(multa)
    
    def guardar_recibo(self, recibo=Recibo):
        if recibo is not None:
            codigo_recibo = recibo.get_codigo()
            if self.buscar_recibo(codigo_recibo) is None:
                self.__recibos.append(recibo)
        else:
            print("No se generó un recibo.")
    # sobre los prestamos
    
    def generar_prestamo(self, lector, libro, fecha_prestamo):
        codigo_prestamo = f"P{self.__nro_prestamos_biblioteca+1}"
        prestamo = Prestamo(codigo_prestamo, lector, libro, fecha_prestamo)
        self.__nro_prestamos_biblioteca += 1
        return prestamo
    
    # Sobre las multas
    
    """
    def calcular_dias_retraso(self, prestamo=Prestamo):
        fecha_devolucion = prestamo.get_fecha_devolucion()
        fecha_entrega_libro = prestamo.get_fecha_entrega()
        dias_retraso = (fecha_entrega_libro - fecha_devolucion)/timedelta(days=1)
        return dias_retraso
    """
    
    def calcular_multa(self, prestamo=Prestamo, lector=Lector):
        
        fecha_devolucion = prestamo.get_fecha_devolucion()
        fecha_entrega_libro = prestamo.get_fecha_entrega()
        
        if fecha_entrega_libro is not None:
            dias_retraso = (fecha_entrega_libro - fecha_devolucion)/timedelta(days=1)
            
            if dias_retraso > 0:
                dias_penalizacion = dias_retraso*2        
                codigo_multa = f"M{self.__nro_multas_biblioteca+1}"
                fecha_inicio = fecha_entrega_libro
                
                fecha_fin = fecha_entrega_libro + timedelta(days=dias_penalizacion)
        
                multa = Multa(codigo_multa, prestamo, lector, dias_penalizacion, fecha_inicio, fecha_fin)
                
                if multa is not None:
                    self.__nro_multas_biblioteca += 1
                    return multa
        
        return None
    
    # sobre los recibos
    
    def generar_recibo(self, objeto=object, lector=Lector):
        nombre_biblioteca = self.__nombre
        codigo_recibo = f"R{self.__nro_recibos_biblioteca+1}"
        fecha_recibo = datetime.today().date()
                    
        if isinstance(objeto, Prestamo):
            
            estado_prestamo = objeto.get_estado_prestamo()
            
            if estado_prestamo != "Atrasado":
            
                if estado_prestamo == "Vigente":
        
                    informacion = f"""Codigo Préstamo: {objeto.get_codigo()}
Titulo Libro: '{objeto.get_libro().get_titulo()}'
Codigo ISBN: {objeto.get_libro().get_codigo_isbn()}
Estado Préstamo: {objeto.get_estado_prestamo()}
Fecha Préstamo: {objeto.get_fecha_prestamo()}
Fecha Devolución: {objeto.get_fecha_devolucion()}"""

                    recibo = Recibo(nombre_biblioteca, codigo_recibo, "Prestamo de Libro" ,fecha_recibo, lector, informacion)
                    self.__nro_recibos_biblioteca += 1

                    if recibo is not None:
                        return recibo
                
                elif estado_prestamo == "Renovado":
                
                    informacion = f"""Codigo Préstamo: {objeto.get_codigo()}
Titulo Libro: '{objeto.get_libro().get_titulo()}'
Codigo ISBN: {objeto.get_libro().get_codigo_isbn()}
Estado Préstamo: {objeto.get_estado_prestamo()}
No. Renovación: {objeto.get_nro_renovaciones()}
Fecha Préstamo: {objeto.get_fecha_prestamo()}
Fecha Devolución Inicial: {objeto.get_fecha_prestamo()+timedelta(days=30)}
Nueva Fecha Devolución: {objeto.get_fecha_devolucion()}"""

                    recibo = Recibo(nombre_biblioteca, codigo_recibo,"Renovacion de Prestamo de Libro", fecha_recibo, lector,informacion)                    
                    
                    if recibo is not None:
                        self.__nro_recibos_biblioteca += 1
                        return recibo

                else: # si el estado del prestamo es "Terminado"
                        
                    informacion = f"""Codigo Préstamo: {objeto.get_codigo()}
Titulo Libro: '{objeto.get_libro().get_titulo()}'
Codigo ISBN: {objeto.get_libro().get_codigo_isbn()}
Estado Préstamo: {objeto.get_estado_prestamo()}
No. Renovaciones Préstamo: {objeto.get_nro_renovaciones()}
Fecha Préstamo: {objeto.get_fecha_prestamo()}
Fecha Devolución: {objeto.get_fecha_devolucion()}
Fecha Entrega: {objeto.get_fecha_entrega()}
Duración Préstamo: {objeto.get_dias_duracion()} dias
Multa: {objeto.comprobar_existencia_multa()}"""
                    
                    recibo = Recibo(nombre_biblioteca, codigo_recibo, "Devolucion de Libro", fecha_recibo,lector,informacion)
                    
                    if recibo is not None:
                        self.__nro_recibos_biblioteca += 1
                        return recibo       
                
        elif isinstance(objeto, Multa):

            informacion = f"""Codigo Multa: {objeto.get_codigo()}
Titulo libro: {objeto.get_prestamo().get_libro().get_titulo()}
Codigo ISBN: {objeto.get_prestamo().get_libro().get_codigo_isbn()}
Dias Penalizacion: {objeto.get_dias_penalizacion()}
Fecha Inicio: {objeto.get_fecha_inicio()}
Fecha Fin: {objeto.get_fecha_fin()}"""

            recibo = Recibo(nombre_biblioteca, codigo_recibo, "Multa", fecha_recibo, lector, informacion)
                                
            if recibo is not None:
                self.__nro_recibos_biblioteca += 1
                return recibo
                
            else:
                print("El estado del prestamo es 'Atrasado'.")
                return None
        else: # si el objeto no es un prestamo o multa
            print("El objeto no es un prestamo o multa.")
            return None
            
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
    
    # Metodos para guardar en archivos
    
    def guardar_lector_en_archivo(self, lector=Lector):
        
        """Guarda la informacion de un lector en el archivo 'lectores.yaml'"""
        
        datos_lector = lector.to_dict() 
        datos = {'lector': datos_lector} 
        
        with open('lectores.yaml','a') as archivo:
            yaml.dump(datos, archivo, default_flow_style=False, allow_unicode=True)
        
    def guardar_bibliotecario_en_archivo(self, bibliotecario=Bibliotecario):
        
        """Guarda la informacion de un bibliotecario en el archivo bibliotecarios.csv"""
        
        datos_bibliotecario = bibliotecario.to_dict()
        
        with open('bibliotecarios.csv','a',newline='',encoding='utf-8') as archivo :
            writer = csv.DictWriter(archivo, fieldnames=datos_bibliotecario.keys())
            
            if archivo.tell() == 0:
               writer.writeheader()

            writer.writerow(datos_bibliotecario)

    def guardar_autor_en_archivo(self, autor=Autor):
        
        """Guarda la informacion de un autor en el archivo autores.csv"""
        
        datos_autor = autor.to_dict()
        
        with open('autores.csv','a',newline='',encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=datos_autor.keys())
            
            if archivo.tell() == 0:
                writer.writeheader()
            
            writer.writerow(datos_autor)
    
    def guardar_prestamo_en_archivo(self, prestamo=Prestamo):
        
        """Guarda la informacion de un prestamo en el archivo prestamos.csv"""
        
        datos_prestamo = prestamo.to_dict()
        
        with open('prestamos.csv','a',newline='',encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=datos_prestamo.keys())
            
            if archivo.tell() == 0:  
                writer.writeheader()
                
            writer.writerow(datos_prestamo) 
        
    def guardar_recibo_en_archivo(self, recibo=Recibo):
        
        """Guarda la informacion de un prestamo en el archivo recibos.yaml"""
        
        datos_recibo = recibo.to_dict()
        datos = {'recibo': datos_recibo}
        with open('recibos.yaml','a') as archivo:
            yaml.dump(datos, archivo, default_flow_style=False, allow_unicode=True)
    
    def guardar_multa_en_archivo(self, multa=Multa):
        
        """Guarda la informacion de una multa en el archivo multas.yaml"""
        
        datos_multa = multa.to_dict()
        datos = {'multa': datos_multa}
        with open('multas.yaml','a') as archivo:
            yaml.dump(datos, archivo, default_flow_style=False, allow_unicode=True)
    
    # Cargar archivos

    def cargar_archivos(self):
        
        """
        Carga todos los datos desde los archivos especificados.
        """
        # Nombres de los archivos
        bibliotecarios_file = 'bibliotecarios.csv'
        autores_file = 'autores.csv'
        lectores_file = 'lectores.yaml'
        prestamos_file = 'prestamos.csv'
        multas_file = 'multas.yaml'
        recibos_file = 'recibos.yaml'

        # Cargar bibliotecarios desde CSV
        with open(bibliotecarios_file, mode='r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    bibliotecario = Bibliotecario.from_dict(fila)
                    self.__bibliotecarios.append(bibliotecario)
                except ValueError as e:
                    print(f"Error al cargar bibliotecario: {e}")

        # Cargar autores desde CSV
        with open(autores_file, mode='r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    autor = Autor.from_dict(fila)
                    self.__autores.append(autor)
                except ValueError as e:
                    print(f"Error al cargar autor: {e}")

        # Cargar lectores desde YAML
        with open(lectores_file, mode='r', encoding='utf-8') as archivo:
            lectores_data = yaml.safe_load(archivo)
            for lector_dict in lectores_data:
                try:
                    lector = Lector.from_dict(lector_dict)
                    self.__lectores.append(lector)
                except ValueError as e:
                    print(f"Error al cargar lector: {e}")

        # Cargar préstamos desde CSV
        with open(prestamos_file, mode='r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    prestamo = Prestamo.from_dict(fila)
                    self.__prestamos.append(prestamo)
                except ValueError as e:
                    print(f"Error al cargar préstamo: {e}")

        # Cargar multas desde YAML
        with open(multas_file, mode='r', encoding='utf-8') as archivo:
            multas_data = yaml.safe_load(archivo)
            for multa_dict in multas_data:
                try:
                    multa = Multa.from_dict(multa_dict)
                    self.__multas.append(multa)
                except ValueError as e:
                    print(f"Error al cargar multa: {e}")

        # Cargar recibos desde YAML
        with open(recibos_file, mode='r', encoding='utf-8') as archivo:
            recibos_data = yaml.safe_load(archivo)
            for recibo_dict in recibos_data:
                try:
                    recibo = Recibo.from_dict(recibo_dict)
                    self.__recibos.append(recibo)
                except ValueError as e:
                    print(f"Error al cargar recibo: {e}")