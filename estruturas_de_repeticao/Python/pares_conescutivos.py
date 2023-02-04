x = 1
soma = 0

while x != 0:
    x = input("Digite um número inteiro: ")
    x = int(x)
    if x % 2 == 0:
        soma = x + (x + 2) + (x+4) + (x + 6) + (x + 8)
    else:
        soma = (x + 1) + (x + 3) + (x + 5 ) +(x + 7) + (x + 9)
    print(f"SOMA = {soma}" )