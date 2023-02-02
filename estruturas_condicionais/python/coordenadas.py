x = input('Valor de X: ')
y = input('Valor de Y: ')

x = float(x)
y = float(y)

eixo_x = (x != 0) and (y == 0)
eixo_y = (y != 0) and (x == 0)
quadrante_1 = (x > 0) and (y > 0)
quadrante_2 = (x < 0) and (y > 0)
quadrante_3 = (x < 0) and (y < 0)
quadrante_4 = (x > 0) and (y < 0 )
origem = (x == 0) and (y == 0)

if eixo_x:
    print("Eixo X")
elif eixo_y:
    print("Eixo Y")
elif quadrante_1:
    print("Q1")
elif quadrante_2:
    print("Q2")
elif quadrante_3:
    print("Q3")
elif quadrante_4:
    print("Q4")
elif origem:
    print("Origem")