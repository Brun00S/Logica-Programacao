salario_atual = input("Digite o salário da pessoa: ")

salario_atual_float = float(salario_atual)

novo_salario = 0
valor_aumento = 0
porcentagem = 0

if salario_atual_float <= 1000:
    porcentagem = 20
    valor_aumento = (salario_atual_float * porcentagem) / 100
    novo_salario = valor_aumento + salario_atual_float

elif (salario_atual_float > 1000) and (salario_atual_float <= 3000):
    porcentagem = 15
    valor_aumento = (salario_atual_float * porcentagem) / 100
    novo_salario = valor_aumento + salario_atual_float

elif (salario_atual_float > 3000) and (salario_atual_float <= 8000):
    porcentagem = 10
    valor_aumento = (salario_atual_float * porcentagem) / 100
    novo_salario = valor_aumento + salario_atual_float

elif salario_atual_float > 8000:
    porcentagem = 15
    valor_aumento = (salario_atual_float * porcentagem) / 100
    novo_salario = valor_aumento + salario_atual_float


print(f'Novo salário = R${novo_salario:.2f}')
print(f'Aumento = R${valor_aumento:.2f}')
print(f'Porcentagem = {porcentagem}%')

