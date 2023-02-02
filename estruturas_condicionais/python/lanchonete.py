codigo_produto = input("Código do Produto Comprado: ")
quantidade_produto = input("Quantidade comprada: ")

quantidade_produto_int = int(quantidade_produto)
preco_produto = 0
total_a_pagar = 0

if codigo_produto == "1":
    preco_produto = 5.00
    total_a_pagar = preco_produto * quantidade_produto_int
elif codigo_produto == "2":
    preco_produto = 3.50
    total_a_pagar = preco_produto * quantidade_produto_int
elif codigo_produto == "3":
    preco_produto = 4.80
    total_a_pagar = preco_produto * quantidade_produto_int
elif codigo_produto == "4":
    preco_produto = 8.90
    total_a_pagar = preco_produto * quantidade_produto_int
elif codigo_produto == "5":
    preco_produto = 7.32
    total_a_pagar = preco_produto * quantidade_produto_int

print(f'Valor a pagar: R${total_a_pagar:.2f}')
