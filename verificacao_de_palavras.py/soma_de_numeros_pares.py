soma = 0
numero = 1

# Usando um laço while para iterar de 1 a 100
while numero <= 100:
    if numero % 2 == 0:  # Verifica se o número é par
        soma += numero   # Soma o número par à variável 'soma'
    numero += 1  # Incrementa o número

# Exibe o resultado da soma
print(f"A soma de todos os números pares de 1 a 100 é: {soma}")
