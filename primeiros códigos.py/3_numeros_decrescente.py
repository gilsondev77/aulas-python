# Entrada de números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Lista com os números
numeros = [numero1, numero2, numero3]

# Ordenação decrescente
numeros.sort(reverse=True)

# Exibindo os números em ordem decrescente
print("Os números em ordem decrescente são:", numeros)
