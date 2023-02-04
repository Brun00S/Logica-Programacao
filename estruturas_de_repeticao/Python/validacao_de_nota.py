nota_1 = input("Digite a primeira nota: ")
nota_1 = float(nota_1)

while nota_1 < 0 or nota_1 > 10:
    nota_1 = input("Valor invalido! Tente novamente: ")
    nota_1 = float(nota_1)

nota_2 = input("Digite a segunda nota: ")
nota_2 = float(nota_2)

while nota_2 < 0 or nota_2 > 10:
    nota_2 = input("Valor invalido! Tente novamente: ")
    nota_2 = float(nota_2)

media = (nota_1 + nota_2) / 2
print(f'MÉDIA = {media:.2f}')

