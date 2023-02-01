base_retangulo = input("Base do Retângulo: ")
altura_retangulo = input("Altura do Retângulo: ")


base_retangulo = float(base_retangulo)
altura_retangulo = float(altura_retangulo)


area_retangulo = base_retangulo * altura_retangulo
perimetro_retangulo = 2 * (base_retangulo + altura_retangulo)
diagonal_retangulo = ((base_retangulo ** 2) + (altura_retangulo ** 2)) ** 0.5

print(f'ÁREA =  {area_retangulo:.4f}')
print(f'PERIMETRO =  {perimetro_retangulo:.4f}')
print(f'Diagonal = {diagonal_retangulo:.4f}')