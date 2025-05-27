numero = int(input('Digite um número: '))

# Variável de controle para contar a partir de 1
contador = 1

# Usando um loop while para iterar até o número fornecido
while contador <= numero:
    if contador % 2 != 0:  # Verifica se o número é ímpar
        print(contador)
    contador += 1  # Incrementa o contador
