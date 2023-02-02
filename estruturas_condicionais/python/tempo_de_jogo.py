hora_inicial = input("Hora Inicial: ")
hora_final = input("Hora Final: ")

hora_inicial = int(hora_inicial)
hora_final = int(hora_final)

duracao_jogo = 0

if hora_inicial > hora_final:
    duracao_jogo = (24 - hora_inicial) + hora_final
elif hora_final > hora_inicial:
    duracao_jogo = hora_final - hora_inicial
else:
    duracao_jogo = 24

print (f'O JOGO DUROU {duracao_jogo} HORAS')