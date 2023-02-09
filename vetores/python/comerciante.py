qtd_produtos = input("Serão digitados dados de quantos produtoa? ")
qtd_produtos = int(qtd_produtos)

total_compra = 0
total_venda = 0
preco_compra = []
preco_venda = []
nome_mercadoria = []
lucro_abaixo_de_10 = 0
lucro_entre_10_e_20 = 0
lucro_acima_de_20 = 0
lucro_total = 0

for i in range(0, qtd_produtos):
    print(f"Produto {i+1}")
    nome_mercadoria.append(input("Nome: "))
    preco_compra.append(float(input("Preço de compra: ")))
    preco_venda.append(float(input("Preço de venda: ")))
    total_compra += preco_compra[i]
    total_venda += preco_venda[i]

    if preco_venda[i] < preco_compra[i] * 1.1:
        lucro_abaixo_de_10 += 1
    elif (preco_venda[i] >= preco_compra[i] * 1.1) and (preco_venda[i] <= preco_compra[i] * 1.2):
        lucro_entre_10_e_20 += 1
    elif preco_venda[i] > preco_compra[i] * 1.2:
        lucro_acima_de_20 += 1


lucro_total = total_venda - total_compra

print()
print('RELATÓRIO')
print(f"Lucro abaixo de 10%: {lucro_abaixo_de_10}")
print(f"Lucro entre 10% e 20%: {lucro_entre_10_e_20}")
print(f"Lucro acima de 20%: {lucro_acima_de_20}")
print(f"Valor total de compra: {total_compra:.2f}")
print(f"Valor total de venda: {total_venda:.2f}")
print(f"Lucro total: {lucro_total:.2f}")
