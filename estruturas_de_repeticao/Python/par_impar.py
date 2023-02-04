n = input("Quantos números você vai digitar? ")

n = int(n)

impar = 0
negativo = 0
positivo = 0
par = 0

for i in range(0, n):
    x = input("Digite um número: ")
    x = int(x)
    
    impar = x % 2 != 0
    par = x % 2 == 0
    negativo = x < 0
    positivo = x > 0
    
    if par and positivo:
        print("PAR POSITIVO")
    elif par and negativo:
        print("PAR NEGATIVO")
    elif impar and positivo:
        print("ÍMPAR POSITIVO")
    elif impar and negativo:
        print("ÍMPAR NEGATIVO")
    elif x == 0:
        print("NULO")
