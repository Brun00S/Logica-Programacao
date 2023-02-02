print("Digite as três distâncias: ")
primeiro_valor = input()
segundo_valor = input()
terceiro_valor = input()

primeiro_valor_float = float(primeiro_valor)
segundo_valor_float = float(segundo_valor)
terceiro_valor_float = float(terceiro_valor)

primeiro_valor_maior = (primeiro_valor_float > segundo_valor_float) and (primeiro_valor_float > terceiro_valor_float)
segundo_valor_maior = (segundo_valor_float > primeiro_valor_float) and (segundo_valor_float > terceiro_valor_float)
terceiro_valor_maior = (terceiro_valor_float > primeiro_valor_float) and (terceiro_valor_float > segundo_valor_float)


if primeiro_valor_maior:
    print(f'MAIOR DISTÂNCIA = {primeiro_valor_float:.2f}')
elif segundo_valor_maior:
    print(f'MAIOR DISTÂNCIA= {segundo_valor_float:.2f}')
elif terceiro_valor_maior:
    print(f'MAIOR DISTÂNCIA = {terceiro_valor_float:.2f}')
else:
    print(f'MAIOR = {primeiro_valor_float:.2f}')
    