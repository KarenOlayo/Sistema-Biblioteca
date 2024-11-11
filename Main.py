from Biblioteca import Biblioteca
from Inventario import Inventario
from Estante import Estante
from Libro import Libro
from Persona import Persona
from Bibliotecario import Bibliotecario
from Lector import Lector
from Autor import Autor
from Multa import Multa
from Recibo import Recibo

class Main:
    
    def run(self):
        
        biblioteca = Biblioteca("Babel","Nechí","Lunes a Viernes 10-12 am")
        inventario = Inventario(biblioteca)
        lector = Lector("Nicole","Adarve","Septiembre","12324234","nico@gmail.com")
        biblioteca.agregar_estante("Ciencias Sociales")
        inventario.agregar_libro("Cien años","12345","Gabo","Ciencias Sociales","Ensayo",14,"Septiembre","Donacion")
        inventario.prestar_libro("Cien años","12345",lector)
    
main = Main()
main.run()