n = input("Quantos casos você vai digitar? ")

n = int(n)

divisao = 0

for i in range(0, n):
    numerador = input("Entre com o numerador: ")
    denominador = input("Entre com o denominador: ")

    numerador = float(numerador)
    denominador = float(denominador)
    
    if denominador == 0:
        print("DIVISÂO IMPOSSÍVEL")
    else:
        divisao = numerador / denominador
        print(f'Divisão = {divisao:.2f}')
