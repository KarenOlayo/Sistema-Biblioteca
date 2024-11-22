
from Biblioteca import Biblioteca
import datetime

class Main:
    
    def run():
        
        biblioteca = Biblioteca("Babel","Puerto Valdivia")
        
        # estantes
        
        biblioteca.agregar_estante("Ciencias Sociales")
        biblioteca.agregar_estante("Ciencias Exactas")
        biblioteca.agregar_estante("Ciencias Humanas")
        biblioteca.agregar_estante("Ciencias Políticas")
        biblioteca.agregar_estante("Literatura")
        
        
        
        #print(biblioteca.get_estantes())
        
        biblioteca.agregar_bibliotecario("Uberney","Perez",datetime.date(1982,6,7),"32534634","uber@gmail.com")
        print(biblioteca.get_bibliotecarios())
        
        # lectores
        
        biblioteca.agregar_lector("Nicole","Adarve", datetime.date(2006,9,9),"12324234","nico@gmail.com")
        biblioteca.agregar_lector("Karen","Vergara", datetime.date(2007,6,3),"2345","karen@gmail.com")
        biblioteca.agregar_lector("Pepe","Martinez", datetime.date(1999,9,9),"3453235","pepemartinez@gmail.com")
        print(biblioteca.get_lectores())
        
        # autores
        
        biblioteca.agregar_autor("Gabo","Gabito","12/9/1984","3/2/2000","Colombia")
        biblioteca.agregar_autor("Lechuza","Perez",datetime.date(1777,7,7),datetime.date(2000,2,2),"Venezuela")
        biblioteca.agregar_autor("Laura","Esquiveq",datetime.date(1998,8,9),datetime.date(2023,12,8),"Canadá")
        print(biblioteca.get_autores())
        
        # agregar libros
                
        biblioteca.agregar_libro("Cien años","01","Gabo Gabito","Literatura","Novela",14,datetime.date(2000,4,5),"Donacion")
        biblioteca.agregar_libro("Cien lagrimas","02","Lechuza Perez","Ciencias Sociales","Enciclopedia",200,datetime.date(2004,9,6),"Donacion")
        biblioteca.agregar_libro("Chocolate con cafe","234","Laura Esquiveq","Ciencias Exactas","Diccionario",444,datetime.date(1888,8,8),"Adquirido por la Biblioteca")    
        
        # prestar libros
        
        biblioteca.prestar_libro("Cien años","01","12324234","13/11/2024")
        biblioteca.prestar_libro("Cien lagrimas","02","2345","14/11/2024")
        biblioteca.prestar_libro("Chocolate con cafe","234","3453235","15/11/2024")
        print(biblioteca.get_libros_prestados())
        
        
        # renovar prestamo de libros
        
        biblioteca.renovar_prestamo("P1","12324234")
        
        # recibir libros devueltos

        biblioteca.recibir_libro_devuelto("P1","12324234","15/11/2024")
        biblioteca.recibir_libro_devuelto("P2","2345","01/01/2025")
        biblioteca.recibir_libro_devuelto("P3","3453235","18/12/2024")
        
        
        # listar 
        
        print(biblioteca.listar_por_autor("Lechuza","Perez"))
        print(biblioteca.listar_por_autor("Gabo","Gabito"))
        print(biblioteca.listar_por_estado("Disponible"))
        print(biblioteca.listar_por_estado("Prestado"))
        print(biblioteca.listar_por_area_del_conocimiento("Ciencias Sociales"))
        print(biblioteca.listar_por_genero("Novela"))
        print(biblioteca.listar_por_fecha_publicacion(datetime.date(1888,8,8)))

Main.run()