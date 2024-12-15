class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, zona):
        self.zonas.append(zona)
        zona.zoologico = self

    def cantidadTotalAnimales(self):
        return sum(zona.cantidadAnimales() for zona in self.zonas)

    def getZona(self):
        return self.zonas