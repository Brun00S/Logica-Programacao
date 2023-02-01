largura_terreno = input("Digite a largura do terreno: ")
comprimento_terreno = input("Digite o comprimento do terreno: ")
valor_metro_quadrado = input("Digite o valor do metro quadrado: ")

largura_terreno = float(largura_terreno)
comprimento_terreno = float(comprimento_terreno)
valor_metro_quadrado = float(valor_metro_quadrado)

area_terreno = largura_terreno * comprimento_terreno
preco_terreno = area_terreno * valor_metro_quadrado

print(f'Area do terreno =  {area_terreno:.2f}')
print(f'Preço do terreno =  {preco_terreno:.2f}')

