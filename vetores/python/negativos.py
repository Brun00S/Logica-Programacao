n = input("Quantos números você vai digitar? ")

n = int(n)
numero_lido = 0
numeros_negativos = []

for i in range(0,n):
    numero_lido = input("Digite um número: ")
    numero_lido = int(numero_lido)
    if numero_lido < 0:
        numeros_negativos.append(numero_lido)

print("NÚMEROS NEGATIVOS: ")
for i in numeros_negativos:
    print(i)