n = input("Quantos casos de teste serão digitados?  ")
n= int(n)

total_cobaias = 0
quantidade_cobaias = 0
total_coelhos = 0
total_sapos = 0
total_ratos = 0
porcentagem_coelhos = 0
porcentagem_ratos = 0
porccentagem_sapos = 0

for i in range(0, n):
    quantidade_cobaias = input ("Quantidade de cobaias: ")
    quantidade_cobaias = int(quantidade_cobaias)
    tipo_cobaia = input("Tipo de cobaia: ")

    if tipo_cobaia == 'C' or tipo_cobaia == 'c':
        total_coelhos += quantidade_cobaias
    elif tipo_cobaia == 'R' or tipo_cobaia == 'r':
        total_ratos += quantidade_cobaias
    elif tipo_cobaia == 'S' or tipo_cobaia == 's':
        total_sapos += quantidade_cobaias
    
    total_cobaias += quantidade_cobaias
    porcentagem_coelhos = (total_coelhos * 100) / total_cobaias
    porcentagem_ratos = (total_ratos * 100) / total_cobaias
    porcentagem_sapos = (total_sapos * 100) / total_cobaias

print("RELATÓRIO FINAL")
print(f'{total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {porcentagem_coelhos:.2f}')
print(f'Percentual de ratos: {porcentagem_ratos:.2f}')
print(f'Percentual de sapos: {porcentagem_sapos:.2f}')
    
