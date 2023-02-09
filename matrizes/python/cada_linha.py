ordem_matriz = input("Qual a ordem da matriz? ")
ordem_matriz = int(ordem_matriz)

matriz = [[0 for x in range(ordem_matriz)] for x in range(ordem_matriz)]
vetor_maiores = []
maior_numero = 0

for i in range(0, ordem_matriz):
    maior_numero = 0
    for j in range(0, ordem_matriz):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))
        if maior_numero < matriz[i][j]:
            maior_numero = matriz[i][j]

    
    vetor_maiores.append(maior_numero)

print("MAIOR DE CADA LINHA: ")
for i in vetor_maiores:
    print(i)

