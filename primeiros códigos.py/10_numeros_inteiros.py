# Inicializar contadores
pares = 0
impares = 0

# Loop para pedir 10 números
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero % 2 == 0:  # Verifica se o número é par
        pares += 1
    else:  # Caso contrário, é ímpar
        impares += 1

# Exibir os resultados
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
