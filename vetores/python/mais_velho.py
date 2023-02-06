numero_pessoas = input("Quantos pessoas você vai digitar? ")
numero_pessoas = int(numero_pessoas)

nomes = []
idade = []
valor_atual = 0
posicao_maior_numero = 0
posicao_atual = 0

for i in range(1, numero_pessoas + 1):
    print(f"Dados da {i}a pessoa:")
    nomes.append(input("Nome: "))
    idade.append(float(input("Idade: ")))

for i in idade:
    if valor_atual < i:
        valor_atual = i
        posicao_maior_numero = posicao_atual
   
    posicao_atual+=1

print(f"PESSOA MAIS VELHA: {nomes[posicao_maior_numero]}")