for i in range(1, 31):  # Inclui o número 30
    if i % 5 == 0:  # Verifica se é múltiplo de 5
        print(f"{i} é múltiplo de 5")
    if i > 20:  # Verifica se o número é maior que 20
        print(f"{i} é maior que 20. Interrompendo o loop.")
        break
