class ContadorPalabras():
    def __init__(self):
        self.contador = 0

    def contar(self,cadena):
        self.contador += len(cadena.split())
        
    def obtener_contador(self):
        return self.contador

cuenta = ContadorPalabras()
cuenta.contar("Cadena de palabras")

print("Se contaron: ",cuenta.obtener_contador(), " palabras")