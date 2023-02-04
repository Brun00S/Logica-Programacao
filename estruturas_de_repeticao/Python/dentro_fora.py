n = input("Quantos numeros você vai digitar? ")

n = int(n)
N = range(n)

contador_dentro = 0
contador_fora = 0

for i in N:
    x = input("Digite um número: ")
    x = int(x)
    if x >= 10 and x <=20:
        contador_dentro += 1
    else:
        contador_fora += 1

print(f'{contador_dentro} DENTRO')
print(f'{contador_fora} FORA')
