senha_digitada = input("Digite a senha: ")

senha_correta = "2002"

while senha_digitada != senha_correta:
    senha_digitada = input("Senha Invalida! Tente novamente: ")
else:
    print("Acesso Permitido")

