from animal import Animal
class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "océano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "océano", genero, "gris", 6)

    @staticmethod
    def cantidadPeces():
        return len(Pez.listado)

    def movimiento(self):
        return "nadar"