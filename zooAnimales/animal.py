from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil

class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__genero = genero
        self.__zona = zona
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return (f"Mamiferos: {Mamifero.cantidadMamiferos()}, "
                f"Aves: {Ave.cantidadAves()}, "
                f"Reptiles: {Reptil.cantidadReptiles()}, "
                f"Peces: {Pez.cantidadPeces()}, "
                f"Anfibios: {Anfibio.cantidadAnfibios()}")

    def toString(self):
        info = f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y mi género es {self.__genero}"
        if self.__zona:
            return f"{info}, la zona en la que me ubico es {self.__zona.getNombre()}, en el {self.__zona.getZoo().getNombre()}."
        return info
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getHabitat(self):
        return self.__habitat
    
    def getGenero(self):
        return self.__genero
    
    def getZona(self):
        return self.__zona
