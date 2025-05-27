while True:
    try:
        numero = int(input("Digite um número (de 1 a 10): "))
        if 1 <= numero <= 10:  # Verifica se o número está no intervalo válido
            print("Número correto.")
            break  # Sai do loop se o número for válido
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")


