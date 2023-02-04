print("Digite dois números:")
x = input()
y = input()

x_int = int(x)
y_int = int(y)

while x_int != y_int:
   
    if x_int < y_int:
      print("CRESCENTE!")
    elif x_int > y_int:
      print("DECRESCENTE !")
    
    print("Digite outros dois números:") 
    x = input()
    y = input()
   
    x_int = int(x)
    y_int = int(y)


