class vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f'El vehiculo es marca {self.marca} y modelo {self.modelo}\n'

a = vehiculo("toyota", 2016)
b = vehiculo("ford", 2020)

print(a)
print(b)

file = open('vehiculo.txt', 'w')
file.write(str(a))
file.write(str(b))



