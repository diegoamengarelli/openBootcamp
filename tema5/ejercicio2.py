while True:
    numero = int(input("Inserte un numero: "))

    def esPrimo(numero):
        if numero < 1:
            return False
        elif numero == 2:
            return True
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    return False
                return True
    print(esPrimo(numero))