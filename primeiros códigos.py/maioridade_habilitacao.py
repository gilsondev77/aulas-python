
# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Solicita se o usuário possui habilitação
habilitacao = input("Você possui habilitação? (sim/não): ").strip().lower()

# Verifica se o usuário é maior de idade e possui habilitação
if idade >= 18 and habilitacao == "sim":
    print("Você é maior de idade e possui habilitação.")
elif idade >= 18 and habilitacao == "não":
    print("Você é maior de idade, mas não possui habilitação.")
elif idade < 18 and habilitacao == "sim":
    print("Você possui habilitação, mas não é maior de idade.")
else:
    print("Você não é maior de idade e também não possui habilitação.")



