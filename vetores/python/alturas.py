n = input("Quantos pessoas serão digitadas? ")
n = int(n)

nomes_maiores_de_16 = []
soma_altura = 0
contagem_maiores_de_16 = 0


for i in range(1,n + 1):
    print(f"Dados da {i}a pessoa:")
    nome = input("Nome: ")
    idade = input("Idade: ")
    altura = input("Altura: ")
    
    idade = int(idade)
    altura = float(altura)
    
    soma_altura += altura

    if idade < 16:
        contagem_maiores_de_16 += 1
        nomes_maiores_de_16.append(nome)


media_altura = soma_altura / n
porcentagem = (contagem_maiores_de_16 * 100) / n


print()
print(f"Altura média: {media_altura:.2f}")
print(f"Pessoas com menos de 16 anos: {porcentagem:.1f}%")

for i in nomes_maiores_de_16:
    print(i)