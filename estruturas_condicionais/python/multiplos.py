print("Digite dois números inteiros:")

numero_1 = input()
numero_2 = input()

numero_1_int = int(numero_1)
numero_2_int = int(numero_2)

if (numero_1_int % numero_2_int == 0) or (numero_2_int % numero_1_int == 0):
    print("São Multiplos")
else:
    print("Não são multiplos")
