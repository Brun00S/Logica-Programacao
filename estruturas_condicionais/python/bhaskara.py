a = input("Coeficiente a: ")
b = input("Coeficiente b: ")
c = input("Coeficiente c: ")

a_float = float(a)
b_float = float(b)
c_float = float(c)

delta = (b_float ** 2) - (4 * a_float * c_float)
raiz_delta = delta ** 0.5
raiz_1 = (- b_float + raiz_delta) / (2 * a_float) 
raiz_2 = (- b_float - raiz_delta) / (2 * a_float)

if delta >= 0:
    print(f'X1 = {raiz_1:.4f}')
    print(f'X2 = {raiz_2:.4f}')
else:
    print("Esta equação não possui raízes reais")