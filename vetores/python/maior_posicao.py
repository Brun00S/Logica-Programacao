n = input("Quantos números você vai digitar? ")
n = int(n)

numeros = []
valor_atual = 0
posicao_maior_numero = 0
posicao_atual = 0

for i in range(0,n):
    numeros.append(float(input("Digite um número: ")))                 

for i in numeros:
    if valor_atual < i:
        valor_atual = i
        posicao_maior_numero = posicao_atual
   
    posicao_atual+=1

print()
print(f"MAIOR VALOR = {valor_atual:.1f}")
print(f"POSIÇÂO DO MAIOR VALOR = {posicao_maior_numero}")

