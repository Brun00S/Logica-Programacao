ordem_matriz = input("Qual a ordem da matriz? ")
ordem_matriz = int(ordem_matriz)

matriz = [[0 for x in range(ordem_matriz)] for x in range(ordem_matriz)]
soma_elementos = 0

for i in range(0, ordem_matriz):
    for j in range(0, ordem_matriz):
        matriz[i][j] = int(input(f"Elemento [{i}, {j}]: "))
        if j - i > 0:
            soma_elementos += matriz[i][j]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma_elementos}")
