from Biblioteca import Biblioteca
from Inventario import Inventario

import datetime

#datetime.date(año, mes, día)

class Main:
    
    def run(self):
        
        biblioteca = Biblioteca("Babel","Puerto Valdivia")
        
        inventario = Inventario(biblioteca)
        
        biblioteca.agregar_lector("Nicole","Adarve",datetime.date(2006,9,9),"12324234","nico@gmail.com")
        biblioteca.agregar_lector("Karen","Vergara",datetime.date(2007,6,3),"2345","karen@gmail.com")
        
        biblioteca.agregar_bibliotecario("Uberney","Perez",datetime.date(1982,6,7),"32534634","uber@gmail.com")
        
        biblioteca.agregar_autor("Gabo","Gabito",datetime.date(1984,4,5),datetime.date(2010,7,3),"Colombia")
        
        biblioteca.agregar_estante("Ciencias Sociales")
        biblioteca.agregar_estante("Ciencias Exactas")
        biblioteca.agregar_estante("Ciencias Humanas")
        biblioteca.agregar_estante("Ciencias Políticas")
        biblioteca.agregar_estante("Literatura")
        
        #print(biblioteca.get_estantes())
                
        inventario.agregar_libro_biblioteca("Cien años","01","Gabo Gabito","Literatura","Ensayo",14,datetime.date(2000,4,5),"Donacion","Disponible")
        inventario.agregar_libro_biblioteca("Cien años","02","Gabo Gabito","Literatura","Ensayo",14,datetime.date(200,5,6),"Donacion","Disponible")        
        
        inventario.prestar_libro("Cien años","01","12324234","13/11/2024","0101")
        inventario.prestar_libro("Cien años","02","12324234","13/11/2024","0101")
                        
        print(biblioteca.buscar_lector("12324234").get_prestamos_vigentes())
        print(biblioteca.buscar_lector("2345").get_prestamos_vigentes())
      
    def cargar_informacion(self):
        pass  
    
main = Main()
main.run()