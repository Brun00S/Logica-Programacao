n = input("Quantos elementos vai ter o vetor? ")
n = int(n)

media_pares = 0
soma_pares = 0
vetor_valores = []
quantidade_de_pares= 0

for i in range(0, n):
    vetor_valores.append(float(input("Digite um número: ")))

    
for i in vetor_valores:
    if i % 2 == 0:
        soma_pares += i
        quantidade_de_pares += 1
        media_pares = soma_pares / quantidade_de_pares





if soma_pares > 0:
    print(f"MÉDIA DOS PARES = {media_pares:.1f}")
else:
    print("NENHUM NÚMERO PAR")


