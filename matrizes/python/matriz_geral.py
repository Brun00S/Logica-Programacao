ordem_matriz = input("Qual a ordem da matriz? ")
ordem_matriz = int(ordem_matriz)

matriz = [[0 for x in range(ordem_matriz)] for x in range(ordem_matriz)]
soma_positivos = 0
diagonal_principal = []
matriz_quadrada = [[0 for x in range(ordem_matriz)] for x in range(ordem_matriz)]
elemento_quadrado = 0
coluna = []


for i in range(0, ordem_matriz):
    for j in range(0, ordem_matriz):
        matriz[i][j] = float(input(f"Elemento [{i}, {j}]: "))
        if matriz[i][j] > 0:
            soma_positivos += matriz[i][j]
        

print(f"SOMA DOS POSITIVOS = {soma_positivos:.1f}")

linha_escolhida = input("Escolha uma linha: ")
linha_escolhida = int(linha_escolhida)
print(f'LINHA ESCOLHIDA: {matriz[linha_escolhida]}')


coluna_escolhida = input("Escolha uma coluna: ")
coluna_escolhida = int(coluna_escolhida)

for i in range(0, ordem_matriz):
    for j in range(0, ordem_matriz):
        if j ==  coluna_escolhida:
            coluna.append(matriz[i][j])

print(f'COLUNA ESCOLHIDA : {coluna}')

for i in range(0, ordem_matriz):
    for j in range(0, ordem_matriz):
        if i == j:
            diagonal_principal.append(matriz[i][j])


print(f"DIAGONAL PRINCIPAL {diagonal_principal}")

for i in range(0, ordem_matriz):
    for j in range(0, ordem_matriz):
        if matriz[i][j] < 0:
            matriz_quadrada[i][j] = matriz[i][j] ** 2
        else:
            matriz_quadrada [i][j] = matriz[i][j]

print(f"MATRIZ ALTERADA : ")
for i in range(0, ordem_matriz):
    print(matriz_quadrada[i])


