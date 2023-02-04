x = 1
y = 1

while x != 0 and y != 0:
    print("Digite os valores das coordendas X e Y:") 
    x = input()
    y = input()
    
    x = float(x)
    y = float(y)
    
    if x > 0 and y > 0:
        print("QUADRANTE 01")
    elif x < 0 and y > 0:
        print("QUADRANTE 02")
    elif x < 0 and y < 0:
        print("QUADRANTE 03")
    elif x > 0 and y < 0:
        print("QUADRANTE 04" )