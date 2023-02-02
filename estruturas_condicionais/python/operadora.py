minutos_usados = input("Digite a quantidade de minutos: ")

minutos_usados_int = int(minutos_usados)

VALOR_MINUTOS_TELEFONIA = 50.00
MINUTOS_TELEFONIA = 100
valor_extra = 2 * (minutos_usados_int % MINUTOS_TELEFONIA)
total = 0


if minutos_usados_int > MINUTOS_TELEFONIA:
    total = VALOR_MINUTOS_TELEFONIA + valor_extra
    print(f"Valor a pagar: R${total:.2f}")
else:
    print(f"Valor a pagar: R${VALOR_MINUTOS_TELEFONIA:.2f}")





