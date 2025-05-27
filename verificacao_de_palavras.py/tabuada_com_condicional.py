numero = int(input("Digite um número para ver a tabuada (apenas múltiplos de 3): "))

# Inicializando o contador
multiplicador = 1

# Laço para calcular e verificar os resultados
while multiplicador <= 10:
    resultado = numero * multiplicador
    if resultado % 3 == 0:  # Verifica se o resultado é múltiplo de 3
        print(f"{numero} x {multiplicador} = {resultado}")
multiplicador += 1  # Incrementa o multiplicador


