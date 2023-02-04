print("Digite dois números: ")
numero_1 = input()
numero_2 = input()

numero_1 = int(numero_1)
numero_2 = int(numero_2)

numero_holder = 0
soma = 0

if numero_1 > numero_2:
    numero_holder = numero_1
    numero_1 = numero_2
    numero_2 = numero_holder


for i in range(numero_1 + 1, numero_2):
    if i % 2 != 0:
        soma = soma + i


print(f'SOMA DOS IMPARES = {soma}')