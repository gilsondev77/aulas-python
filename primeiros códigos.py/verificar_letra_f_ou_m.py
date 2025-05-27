# Entrada de dados
letra = input("Digite uma letra (F ou M): ").strip().upper()

# Verificação da letra
if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")
