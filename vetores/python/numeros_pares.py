n = input("Quantos números você vai digitar? ")
n = int(n)

numeros = []
numeros_pares = []
contagem_pares = 0
numero = 0

for i in range(0,n):
    numeros.append(int(input("Digite um número: ")))


for i in numeros:
    if i % 2 == 0:
        numeros_pares.append(i)
        contagem_pares +=1

print()
print("NÚMEROS PARES: ")
print(numeros_pares)
print(f'QUANTIDADE DE PARES = {contagem_pares}')


