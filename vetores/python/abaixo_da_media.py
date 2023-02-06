n = input("Quantos elementos tem esse vetor? ")
n = int(n)

media_vetor = 0
soma_valores = 0
vetor_valores = []

for i in range(0, n):
    vetor_valores.append(float(input("Digite um número: ")))

for i in vetor_valores:
    soma_valores += i

media_vetor = soma_valores / n

print()
print(f"MÉDIA DO VETOR = {media_vetor}")
print(f"ELEMENTOS ABAIXO DA MÉDIA:")

for i in vetor_valores:
    if i < media_vetor:
        print(i)


