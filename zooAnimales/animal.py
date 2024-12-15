from anfibio import Anfibio
from ave import Ave
from reptil import Reptil
from mamifero import Mamifero
from pez import Pez
class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.totalAnimales += 1

    def __str__(self):
        base = f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}"
        if self.zona:
            return f"{base}, la zona en la que me ubico es {self.zona.nombre}, en el {self.zona.zoologico.nombre}."
        return base

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return f"Mamíferos: {Mamifero.cantidadMamiferos()}, Aves: {Ave.cantidadAves()}, Reptiles: {Reptil.cantidadReptiles()}, Peces: {Pez.cantidadPeces()}, Anfibios: {Anfibio.cantidadAnfibios()}"

