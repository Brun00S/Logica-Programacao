n = input("Quantos valores vai ter cada vetor? ")
n = int(n)

vetorA = []
vetorB = []
vetorC = []
soma = 0

print("Digite os valores do vetor A:")
for i in range(0,n):
    vetorA.append(int(input()))

print("Digite os valores do vetor B:")
for i in range(0,n):
    vetorB.append(int(input()))

for i in range(0,n):
    soma = vetorA[i] + vetorB[i]
    vetorC.append(soma)

print("VETOR RESULTANTE:")
for i in vetorC:
    print(i)


