from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guaw"

class Gato(Animal):
    def hablar(self):
        return "Miaw"
    
perro1 = Perro("Firulais")
gato1 = Gato("Michi")

print("El perro ",perro1.nombre, "hace: ", perro1.hablar())
print("El gato ",gato1.nombre, "hace: ", gato1.hablar())