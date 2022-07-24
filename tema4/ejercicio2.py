numero_inicial = int(input("Ingrese un numero inicial: "))
numero_final = int(input("Ingrese un numero final: "))
impares = []
for i in range(numero_inicial,numero_final+1):
    if (i % 2 != 0):
        impares.append(i)
    else: continue
print(impares)
