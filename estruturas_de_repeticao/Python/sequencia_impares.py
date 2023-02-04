x = input("Digite o valor de X: ")
x = int(x)


for i in range(1, x):
    if i % 2 != 0:
        print(i)

if x % 2 != 0:
    print(x)