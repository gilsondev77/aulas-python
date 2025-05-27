positivos = 0
negativos = 0

print("Digite até 10 números. O programa será interrompido se o número 0 for inserido.")
for i in range(10):  # Loop para permitir 10 entradas
    numero = int(input(f"Digite o número {i + 1}: "))
    if numero == 0:
        print("Número 0 inserido. Fim do programa.")
        break
    elif numero > 0:
        positivos += 1
    else:
        negativos += 1

print(f"\nTotal de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")
