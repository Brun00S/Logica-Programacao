distancia_percorrida = input("Distância Percorrida: ")
combustivel_gasto = input("Combustível gasto: ")

distancia_percorrida = float(distancia_percorrida)
combustivel_gasto = float(combustivel_gasto)

consumo_medio = distancia_percorrida / combustivel_gasto

print(f'Consumo médio = {consumo_medio:.3f}')