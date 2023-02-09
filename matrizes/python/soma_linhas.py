linhas = input("Qual a quantidade de linhas da matriz? ")
colunas = input("Qual a quantidade de colunas da matriz? ")
linhas = int(linhas)
colunas = int(colunas)

matriz = [[0 for x in range(colunas)] for x in range(linhas)]
vetor = []
soma_elementos_matriz = 0

for i in range(0, linhas):
    print(f'Digite os elementos da {i+1}. linha:')
    soma_elementos_matriz = 0
    for j in range(0, colunas):
        matriz[i][j] = float(input())
        soma_elementos_matriz += matriz[i][j]
        
    vetor.append(soma_elementos_matriz)

print("VETOR GERADO:")
for i in vetor:
    print(i)
        
