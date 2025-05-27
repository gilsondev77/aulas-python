while True:
    numero = int(input("Digite um número (ou um número negativo para sair): "))
    if numero < 0:
        print("Número negativo detectado. Encerrando o programa.")
        break
    else:
        print(f"Você digitou: {numero}")

