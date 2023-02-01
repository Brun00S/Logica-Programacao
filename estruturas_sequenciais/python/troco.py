preco_unidade_produto = input("Preço unitário do produto: ")
quantidade_comprada = input("Quantidade comprada: ")
dinheiro_recebido = input("Dinheiro recebido: ")

preco_unidade_produto = float(preco_unidade_produto)
quantidade_comprada = int(quantidade_comprada)
dinheiro_recebido = float(dinheiro_recebido)

troco = dinheiro_recebido - (preco_unidade_produto * quantidade_comprada)

print(f'TROCO = {troco:.2f}')