primeira_nota = input("Digite a primeira nota: ")
segunda_nota = input("Digite a segunda nota: ")

primeira_nota_float = float(primeira_nota)
segunda_nota_float = float(segunda_nota)

nota_final = primeira_nota_float + segunda_nota_float

print(f"NOTA FINAL = {nota_final:.1f}")

if nota_final < 60.00:
    print ("REPROVADO!")




