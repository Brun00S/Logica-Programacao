qta_pessoas = int(input("Quantas pessoas serão digitadas? "))


media_altura_mulheres = 0
total_altura_mulheres = 0
contagem_mulheres = 0
contagem_homens = 0
altura = []
sexo = []

for i in range(0, qta_pessoas):
    altura.append(float(input(f"Altura da {i+1}a pessoa: ")))
    sexo.append(input(f"Sexo da {i+1}a pessoa: "))


    if sexo[i] == "F" or sexo[i] == "f":
        contagem_mulheres += 1
        total_altura_mulheres += altura[i]
    elif sexo[i] == "M" or sexo[i] == "m":
        contagem_homens += 1


media_altura_mulheres = total_altura_mulheres / contagem_mulheres
altura.sort()
print()
print(f"Menor altura = {altura[0]:.2f}")
print(f"Maior altura = {altura[-1]:.2f}")
print(f"Média das alturas das mulheres = {media_altura_mulheres:.2f} ")
print(f"Número dos homens = {contagem_homens}")

