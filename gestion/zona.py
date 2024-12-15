class Zona:
    def __init__(self, nombre, zoo=None):
        self.__nombre = nombre
        self.__zoo = zoo
        self.__animales = []

    def agregarAnimales(self, animal):
        self.__animales.append(animal)

    def cantidadAnimales(self):
        return len(self.__animales)

    def getZoo(self):
        return self.__zoo

