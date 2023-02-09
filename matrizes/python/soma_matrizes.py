linhas = input("Qual a quantidade de linhas da matriz? ")
colunas = input("Qual a quantidade de colunas da matriz? ")
linhas = int(linhas)
colunas = int(colunas)

matriz_A = [[0 for x in range(colunas)] for x in range(linhas)]
matriz_B = [[0 for x in range(colunas)] for x in range(linhas)]
matriz_C = [[0 for x in range(colunas)] for x in range(linhas)]

print("Digite os valores da matriz A:")
for i in range(0, linhas):
    for j in range(0, colunas):
        matriz_A[i][j] = int(input(f"Elemento [{i},{j}]: "))


print("Digite os valores da matriz B:")
for i in range(0, linhas):
    for j in range(0, colunas):
        matriz_B[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("MATRIZ SOMA:")
for i in range(0, linhas):
    for j in range(0, colunas):
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]

for i in range(0, linhas):
    print(matriz_C[i])
