class Zona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []
        self.zoologico = None

    def agregarAnimales(self, animal):
        self.animales.append(animal)
        animal.zona = self

    def cantidadAnimales(self):
        return len(self.animales)
