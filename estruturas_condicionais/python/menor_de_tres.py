primeiro_valor = input("Primeiro Valor: ")
segundo_valor = input("Segundo Valor: ")
terceiro_valor = input("Terceiro Valor: ")

primeiro_valor_int = int(primeiro_valor)
segundo_valor_int = int(segundo_valor)
terceiro_valor_int = int(terceiro_valor)

primeiro_valor_menor = (primeiro_valor_int < segundo_valor_int) and (primeiro_valor_int < terceiro_valor_int)
segundo_valor_menor = (segundo_valor_int < primeiro_valor_int) and (segundo_valor_int < terceiro_valor_int)
terceiro_valor_menor = (terceiro_valor_int < primeiro_valor_int) and (terceiro_valor_int < segundo_valor_int)


if primeiro_valor_menor:
    print(f'MENOR = {primeiro_valor_int}')
elif segundo_valor_menor:
    print(f'MENOR = {segundo_valor_int}')
elif terceiro_valor_menor:
    print(f'MENOR = {terceiro_valor_int}')
else:
    print(f'MENOR = {primeiro_valor_int}')
    