codigo_combustivel = 0
contador_alcool = 0
contador_gasolina = 0
contador_diesel = 0

while codigo_combustivel != 4:
    codigo_combustivel = input("Informe um código (1, 2, 3)  ou 4 para parar: ")
    codigo_combustivel = int(codigo_combustivel)
    if codigo_combustivel == 1:
        contador_alcool += 1
    elif codigo_combustivel == 2:
        contador_gasolina += 1
    elif codigo_combustivel == 3:
        contador_diesel += 1

print("MUITO OBRIGADO!")
print(f'Alcool: {contador_alcool}')
print(f'Gasolina: {contador_gasolina}')
print(f'Diesel: {contador_diesel}')