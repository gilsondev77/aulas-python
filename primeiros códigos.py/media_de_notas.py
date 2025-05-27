# Variáveis para armazenar a soma das notas e o contador
soma_notas = 0
contador = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para sair): "))
    if nota == -1:  # Verifica se o usuário deseja sair
        break
    elif nota >= 0:  # Apenas considera notas válidas (não negativas)
        soma_notas += nota
        contador += 1
    else:
        print("Nota inválida! Digite uma nota válida ou -1 para sair.")

# Calcula e exibe a média, se houver notas válidas
if contador > 0:
    media = soma_notas / contador
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
