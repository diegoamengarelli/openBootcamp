class Vehiculo():

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas, self.puertas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} ruedas, {} puertas, {} cc, {} km/h".format( self.color, self.ruedas, self.puertas, self.cilindrada, self.velocidad)

c = Coche("Azul", 4, 5, 120, 1500)

print(c)