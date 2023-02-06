n = input("Quantos números você vai digitar? ")
n = int(n)

valores = []
soma = 0

for i in range(0,n):
    numero_lido = input("Digite um número: ")
    numero_lido = float(numero_lido)
    valores.append(numero_lido)
    soma += numero_lido

media = soma / n

print(f"VALORES = {valores}")
print(f"SOMA = {soma:.2f}")
print(f"MÉDIA = {media:.2f}")
