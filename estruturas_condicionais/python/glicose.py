glicose = input("Digite a medida de glicose: ")

glicose_float = float(glicose)

if glicose_float <= 100:
    print("Classificado: normal")
elif (glicose_float > 100) and (glicose_float <= 140):
    print("Classficado: elevado")
else:
    print("Classificado: diabetes")