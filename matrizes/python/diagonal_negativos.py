ordem_matriz = input("Qual a ordem da matriz? ")
ordem_matriz = int(ordem_matriz)

matriz = [[0 for x in range(ordem_matriz)] for x in range(ordem_matriz)]
diagonal_principal = []
contagem_negativos = 0

for i in range(0, ordem_matriz):
    for j in range(0, ordem_matriz):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))
        if i == j:
            diagonal_principal.append(matriz[i][j])
        
        if matriz[i][j] < 0:
            contagem_negativos +=1

print("DIAGONAL PRINCIPAL: ")
print(diagonal_principal)
print(f"QUANTIDADE DE NEGATIVOS: {contagem_negativos}")


