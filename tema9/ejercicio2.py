from functools import reduce

lista = [1, 3, 5, 55, 67, 24, 0, 7, 9]

def function(lista): 
    resultado = list(filter((lambda x: x % 2), lista)) 
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(f'La suma es: {resultado}')


function(lista)