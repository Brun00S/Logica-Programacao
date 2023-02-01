nome = input("Nome: ")
valor_hora = input("Valor por hora: ")
horas_trabalhadas = input("Horas trabalhadas: ")

valor_hora = float(valor_hora)
horas_trabalhadas = float(horas_trabalhadas)

pagamento_funcionario = valor_hora * horas_trabalhadas

print(f'O pagamento para {nome} deve ser {pagamento_funcionario:.2f}')