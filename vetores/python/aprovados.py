qtd_alunos = int(input("Quantos alunos serão digitados? "))


nome = []
nota1 = []
nota2 = []
media = []
soma_notas = 0
nome_aprovados = []

for i in range(0, qtd_alunos):
    print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno:")
    nome.append(input())
    nota1.append(float(input()))
    nota2.append(float(input()))
    media.append((nota1[i] + nota2[i])/2)
    if media[i] >= 6:
        nome_aprovados.append(nome[i])
        
print("Alunos aprovados:")
for i in nome_aprovados:
    print(i)





