from DataInicial import TIPOS_DE_RECIBOS
class Recibo:
    
    def __init__(self, tipo):
        
        while True:
            if tipo in TIPOS_DE_RECIBOS:
                self.__tipo = tipo
                break
            else:
                print(f"El tipo de recibo {tipo} es invalido. Intente nuevamente")
                
# Metodos Accesores y Modificadores

def get_tipo(self):
        return self.__tipo
    
def set_tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

def imprimir_recibo():
    pass