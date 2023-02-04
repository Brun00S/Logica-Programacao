n = input("Quantos casos você vai digitar? ")

n = int(n)

soma_notas = 0
media_notas = 0
pesos_notas = 0



for i in range(0, n):
    print("Digite três números: ")
    nota_1 = input()
    nota_2 = input()
    nota_3 = input()

    nota_1 = float(nota_1)
    nota_2 = float(nota_2)
    nota_3 = float(nota_3)
    
    soma_notas = (nota_1 * 2) + (nota_2 * 3) + (nota_3 * 5)
    media_notas = soma_notas / 10
    
    print(f'MÉDIA = {media_notas:.1f}')