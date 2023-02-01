print("Dados da primeira pessoa:")
nome_primeira_pessoa = input("Nome: ")
idade_primeira_pessoa = input("Idade: ")

print("Dados da segunda pessoa:")
nome_segunda_pessoa = input("Nome: ")
idade_segunda_pessoa = input("Idade: ")

idade_primeira_pessoa = float(idade_primeira_pessoa)
idade_segunda_pessoa = float(idade_segunda_pessoa)

media_idade = (idade_primeira_pessoa + idade_segunda_pessoa) / 2

print(f'A idade média de {nome_primeira_pessoa} e {nome_segunda_pessoa} é {media_idade:.1f}')

