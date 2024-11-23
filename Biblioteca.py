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
        
        self.__libros = np.full((500), fill_value=None , dtype=Libro)
        self.__nro_libros = 0
        
        self.__libros_prestados = []
        self.__libros_disponibles = []
        
        self.__bibliotecarios = []
        self.__lectores = []
        self.__autores = []
        
        self.__recibos = []
        self.__nro_recibos_biblioteca = 0
        
        self.__multas = []
        self.__nro_multas_biblioteca = 0
        
        self.__prestamos = []
        self.__nro_prestamos_biblioteca = 0
                
    # Metodos Accesores

    def get_nombre(self):
        return self.__nombre

    def get_ubicacion(self):
        return self.__ubicacion
    
    def get_estantes(self):
        return self.__estantes
    
    def get_nro_estantes(self):
        return self.__nro_estantes
    
    def get_libros(self):
        return self.__libros
    
    def get_nro_libros(self):
        return self.__nro_libros
    
    def get_libros_prestados(self):
        return self.__libros_prestados
    
    def get_libros_disponibles(self):
        return self.__libros_disponibles
    
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
    
    def buscar_libro(self, titulo, codigo_isbn): 
        for indice, libro in enumerate(self.__libros):
            if indice >= self.__nro_libros: #¿>= o > ?
                break
            if libro is not None and libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                return indice, libro 
        return -1 , None 
    
    def buscar_libro_disponible(self, titulo, codigo_isbn):
        for libro in self.__libros_disponibles:
            if libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                return libro
        return None
    
    def buscar_libro_prestado(self, titulo, codigo_isbn):
        for libro in self.__libros_prestados:
            if libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                return libro
        return None
        
    def verificar_autor(self, autor:str): # se ingresa el nombre y apellido del autor separado por espacio
        nombre_apellido = autor.split()
        if len(nombre_apellido) == 2:
            nombre, apellido = nombre_apellido
            obj_autor = self.buscar_autor(nombre, apellido)
            if obj_autor is not None:
                return obj_autor
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
            print(f"Autor {nombre} {apellido} agregado con exito")

    def agregar_lector(self, nombre, apellido, fecha_nacimiento, identificacion, email):
        if self.buscar_lector(identificacion) == None :
            lector = Lector(nombre, apellido, fecha_nacimiento, identificacion, email)
            self.__lectores.append(lector)
            print(f"Lector {nombre} agregado.")
    
    def agregar_libro(self, titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, anio_publicacion, origen):
        _, libro = self.buscar_libro(titulo, codigo_isbn)
        if libro is None:
            autor_valido = self.verificar_autor(autor)
            if autor_valido is not None:
                if self.__nro_libros < len(self.__libros):
                    libro = Libro(titulo, codigo_isbn, autor, area_del_conocimiento, genero, nro_paginas, anio_publicacion, origen)
                    self.__libros[self.__nro_libros] = libro 
                    self.__nro_libros += 1 
                    self.agregar_libro_estante(area_del_conocimiento, libro)
                    print("Libro agregado con éxito.")
            else:
                print("El autor no está registrado.")
        else:
            print("El libro ya existe.")
                
    def agregar_libro_estante(self, area_del_conocimiento, libro:Libro):
        _, estante = self.buscar_estante(area_del_conocimiento)
        if estante is not None:
            if estante.get_nro_libros_estante() < len(estante.get_libros_estante()):
                estante.get_libros_estante()[estante.get_nro_libros_estante()] = libro
                estante.incrementar_nro_libros_estante() #suma 1 al nro de libros del estante
    
    def agregar_libro_disponible(self, libro=Libro):
        titulo = libro.get_titulo()
        codigo_isbn = libro.get_codigo_isbn()
        
        if self.buscar_libro_disponible(titulo, codigo_isbn) is None:
            self.__libros_disponibles.append(libro)
            return True
        return False
    
    def agregar_libro_prestado(self, libro=Libro):
        titulo = libro.get_titulo()
        codigo_isbn = libro.get_codigo_isbn()
        
        if self.buscar_libro_prestado(titulo, codigo_isbn) is None:
            self.__libros_prestados.append(libro)
            return True
        return False
    
    def eliminar_libro(self, titulo, codigo_isbn):        
        indice, libro = self.buscar_libro(titulo, codigo_isbn)
        if libro is not None:
            area_del_conocimiento = libro.get_area_del_conocimiento()
            _, estante = self.buscar_estante(area_del_conocimiento)
            if indice != -1:
                for i in range(indice, self.__nro_libros-1):
                    self.__libros[i] = self.__libros[i+1]
                self.__libros[self.__nro_libros-1] = None 
                self.__nro_libros -= 1
            
                estante.eliminar_libro_estante(titulo, codigo_isbn)
                print("Libro eliminado de la biblioteca.")
                
    def eliminar_libro_disponible(self, titulo, codigo_isbn):
        for libro in self.__libros_disponibles:
            if libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                self.__libros_disponibles.remove(libro)
    
    def eliminar_libro_prestado(self, titulo, codigo_isbn):
        for libro in self.__libros_prestados:
            if libro.get_titulo() == titulo and libro.get_codigo_isbn() == codigo_isbn:
                self.__libros_prestados.remove(libro)
    
    # Metodos funcionales
    
    def prestar_libro(self, titulo, codigo_isbn, identificacion_lector, fecha_prestamo):
        
        lector = self.buscar_lector(identificacion_lector) #retorna un objeto
        
        if lector is None:
            print(f"No se puede realizar el préstamo. Lector {identificacion_lector} no encontrado.")
            return
        
        lector_cumple_requisitos = lector.verificar_requisitos_prestamo()
        
        if lector_cumple_requisitos == False:
            print(f"No se puede realizar el préstamo. Lector {identificacion_lector} no cumple con los requisitos para el préstamo.")
            return
        
        indice, libro = self.buscar_libro(titulo, codigo_isbn)
        
        if indice == -1 and libro is None:
            print(f"No se puede realizar el préstamo. Libro {titulo} no encontrado.")
            return
        
        if libro.get_estado() == "Disponible":
            
            libro.set_estado("Prestado")
    
            prestamo = self.generar_prestamo(lector, libro, fecha_prestamo)
            recibo = self.generar_recibo(prestamo, lector)
            
            self.guardar_prestamo(prestamo)
            self.guardar_recibo(recibo)
                            
            lector.guardar_prestamo(prestamo)
            lector.guardar_recibo(recibo)
            lector.agregar_libro_a_prestamos_vigentes(libro)
            
            self.eliminar_libro_disponible(titulo, codigo_isbn)
            self.agregar_libro_prestado(libro)
                            
            print("Préstamo realizado con éxito.")
            print(recibo)
        
    def renovar_prestamo(self, codigo_prestamo, identificacion_lector):
        lector = self.buscar_lector(identificacion_lector)
        prestamo = self.buscar_prestamo(codigo_prestamo)
        
        if prestamo is None:
            print(f"El préstamo {codigo_prestamo} no existe. No se pudo renovar el préstamo.")
            return
        
        estado_prestamo = prestamo.get_estado_prestamo()
        
        if lector is not None:
            if prestamo is not None and estado_prestamo == "Vigente":
                cumple_requisitos = lector.verificar_requisitos_renovacion(codigo_prestamo)
                if cumple_requisitos == True:
                    fecha_devolucion_inicial = prestamo.get_fecha_devolucion()
                    nueva_fecha_devolucion = fecha_devolucion_inicial + timedelta(days=30)
                    prestamo.set_fecha_devolucion(nueva_fecha_devolucion)
                    prestamo.incrementar_nro_renovaciones()
                    prestamo.set_estado("Renovado")
                    
                    recibo = self.generar_recibo(prestamo, lector)
                    self.guardar_recibo(recibo)
                    lector.guardar_recibo(recibo)
                    
                    print("Prestamo renovado exitosamente.")
                    print(recibo)
    
    def recibir_libro_devuelto(self, codigo_prestamo, identificacion_lector, fecha_entrega):
        
        lector = self.buscar_lector(identificacion_lector)
        prestamo = self.buscar_prestamo(codigo_prestamo)
        fecha_prestamo  = prestamo.get_fecha_prestamo()
        
        if prestamo is not None:
            if lector is not None:
                if datetime.strptime(fecha_entrega, '%d/%m/%Y').date() >= fecha_prestamo:
                    if prestamo.get_lector().get_identificacion() == identificacion_lector:
                        libro = prestamo.get_libro()
                        if libro is not None:
                            libro.set_estado("Disponible")
                
                            self.eliminar_libro_prestado(libro.get_titulo(),libro.get_codigo_isbn())
                            self.agregar_libro_disponible(libro)
            
                            lector.eliminar_libro_de_prestamos_vigentes(libro)                    
                        
                            prestamo.set_fecha_entrega(fecha_entrega)
                            prestamo.set_estado("Terminado")
                                            
                            multa = self.calcular_multa(prestamo, lector)
                            if multa is not None:
                                prestamo.set_multa(multa)
                                lector.guardar_multa(multa)
                                self.guardar_multa(multa)
                                #print(multa)
                    
                                recibo_multa = self.generar_recibo(multa, lector)
                                self.guardar_recibo(recibo_multa)
                                lector.guardar_recibo(recibo_multa)
                                print(recibo_multa)
                
                            recibo_devolucion = self.generar_recibo(prestamo,lector)
                            self.guardar_recibo(recibo_devolucion)
                            lector.guardar_recibo(recibo_devolucion)
                            print("Libro devuelto exitosamente.")
                            print(recibo_devolucion)   
                            
                        else:
                            print("El libro del préstamo no es válido.")
                    else:
                        print(f"El lector {identificacion_lector} no corresponde con el lector del préstamo {codigo_prestamo}")
                else:
                    print("La fecha de entrega es anterior a la fecha de préstamo.")
            else:
                print(f"El lector con identificación {identificacion_lector} no existe")
        else:
            print(f"El préstamo {codigo_prestamo} no existe")
   
    # Metodos para listar
    
    def listar_por_estado(self,estado):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro] is not None and self.__libros[libro].get_estado() == estado:
                if estado == "Disponible" :
                    listado_libros.append(self.__libros[libro])
                if estado == "Prestado" :
                    listado_libros.append(self.__libros[libro])
        return listado_libros
    
    def listar_por_autor(self, nombre, apellido):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro] is not None:
                autor = self.__libros[libro].get_autor()
                if f"{nombre} {apellido}" == autor:
                    listado_libros.append(self.__libros[libro])
        return listado_libros
    
    def listar_por_area_del_conocimiento(self, area_del_conocimiento):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro].get_area_del_conocimiento() == area_del_conocimiento:
                listado_libros.append(self.__libros[libro])
        return listado_libros
    
    def listar_por_genero(self, genero):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro].get_genero() == genero:
                listado_libros.append(self.__libros[libro])
        return listado_libros
    
    def listar_por_anio_publicacion(self, anio_publicacion):
        listado_libros = []
        for libro in range(self.__nro_libros):
            if self.__libros[libro].get_anio_publicacion() == anio_publicacion:
                listado_libros.append(self.__libros[libro])
        return listado_libros
    
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
    
    
    def calcular_dias_retraso(self, prestamo=Prestamo):
        fecha_devolucion = prestamo.get_fecha_devolucion()
        fecha_entrega_libro = prestamo.get_fecha_entrega()
        if fecha_entrega_libro is not None:
            dias_retraso = (fecha_entrega_libro - fecha_devolucion)/timedelta(days=1)
            return dias_retraso
        else:
            return None
    
    def calcular_multa(self, prestamo=Prestamo, lector=Lector):
        
        fecha_entrega_libro = prestamo.get_fecha_entrega()
        
        if fecha_entrega_libro is not None:
            dias_retraso = self.calcular_dias_retraso(prestamo)
            
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
Dias Retraso: {int(self.calcular_dias_retraso(objeto))} dias
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
            print(f"Autor {nombre} {apellido} eliminado con exito.")