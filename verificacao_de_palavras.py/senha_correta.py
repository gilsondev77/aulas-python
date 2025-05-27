senha_correta = "1234"  # Definindo a senha correta como uma string

while True:
    senha = input("Digite a senha: ")  # Solicita a senha do usuário
    if senha == senha_correta:  # Verifica se a senha está correta
        print("Senha correta! Acesso concedido.")
        break  # Sai do loop se a senha estiver correta
    else:
        print("Senha incorreta. Tente novamente.")


