## Encapsulamiento
## Se colocan 2 guion bajo al nombre de la variable para volverla inmutable, 
## puede ser alterada desde dentro, pero no puedes tocarla desde fuera

class encap:
    def __init__(self):
        self.__numero = 0

    def operacion(self):
        print(self.__numero + 20)

    def resultado(self):
        return self.__numero
    
ejemplo = encap

ejemplo.operacion()
print(ejemplo.resultado())

## se puede llamar a los metodos pero no alterar directamente las variables
## ejemplo.__numero = 100

