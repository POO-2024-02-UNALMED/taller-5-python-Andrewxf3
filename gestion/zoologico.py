class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__zonas = []

    def agregarZonas(self, zona):
        self.__zonas.append(zona)

    def cantidadTotalAnimales(self):
        return sum(zona.cantidadAnimales() for zona in self.__zonas)

    def getZona(self):
        return self.__zonas
