duracao_segundos = input("Digite a duração em segundos: ")

duracao_segundos = int(duracao_segundos)

horas = duracao_segundos // 3600
minutos = (duracao_segundos % 3600) // 60
segundos = (duracao_segundos % 3600) % 60

print(f'{horas}:{minutos}:{segundos}')