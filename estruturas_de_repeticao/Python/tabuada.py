numero_tabuada = input("Deseja a tabuda para qual valor? ")

numero_tabuada = int(numero_tabuada)

multiplicando = range(1,11)
resultado = 0

for i in multiplicando:
    resultado = numero_tabuada * i
    print(f'{numero_tabuada} x {i} = {resultado}')
    