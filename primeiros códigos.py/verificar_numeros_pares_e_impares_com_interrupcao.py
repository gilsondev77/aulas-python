for i in range(1, 21):  # Ajustei para incluir o número 20
    if i == 15:  # Verifica se o número é 15 antes de qualquer outra coisa
        print("Número 15 encontrado, interrompendo o loop.")
        break
    elif i % 2 == 0:
        print(f"{i} é número par.")
    else:
        print(f"{i} é número ímpar.")
