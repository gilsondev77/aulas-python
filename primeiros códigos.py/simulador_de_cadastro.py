# Solicitar cadastro de senha
senha = input("Cadastre sua senha: ")

# Solicitar confirmação da senha
confirmacao = input("Confirme sua senha: ")

# Verificar se as senhas coincidem
if senha == confirmacao:
    print("Senha correta. Bem-vindo!")
else:
    print("Senha incorreta. Tente novamente.")
