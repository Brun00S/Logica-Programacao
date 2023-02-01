a = input("Digite a medida A: ")
b = input("Digite a medida B: ")
c = input("Digite a medida C: ")

a = float(a)
b = float(b)
c = float(c)

area_quadrado = a ** 2
area_triangulo_retangulo = (a * b) / 2
area_trapezio = ((a + b) * c) / 2

print(f'ÁREA DO QUADRADO = {area_quadrado:.4f}')
print(f'ÁREA DO TRIÂNGULO = {area_triangulo_retangulo:.4f}')
print(f'ÁREA DO TRAPÉZIO = {area_trapezio:.4f}')