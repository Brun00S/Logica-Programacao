linhas = input("Qual a quantidade de linhas da matriz? ")
colunas = input("Qual a quantidade de colunas da matriz? ")
linhas = int(linhas)
colunas = int(colunas)

matriz = [[0 for x in range(colunas)] for x in range(linhas)]
negativos = []

for i in range(0, linhas):
    for j in range(0, colunas):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))
        if matriz[i][j] < 0:
            negativos.append(matriz[i][j])

print('VALORES NEGATIVOS: ')
for i in negativos:
    print(i)
