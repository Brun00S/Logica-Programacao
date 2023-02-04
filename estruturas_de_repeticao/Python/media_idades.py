print("Digite as idades: ")

contagem_numeros = 0
soma_numeros = 0
numero = 0
media = 0
 
numero = input()
numero = int(numero)

if numero < 0:
    print("IMPOSSÌVEL DE CALCULAR")
else:
    while numero >= 0:
        soma_numeros = soma_numeros + numero
        contagem_numeros += 1
        media = soma_numeros / contagem_numeros
        numero = input()
        numero = int(numero)
    print(f'MÉDIA = {media:.2f}')

