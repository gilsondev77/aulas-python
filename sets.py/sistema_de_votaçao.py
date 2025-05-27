# Dicionário com as opções de voto
votos = {
    '1': 0,  # Candidato A
    '2': 0,  # Candidato B
    '3': 0   # Candidato C
}

print("=== Sistema de Votação ===")
print("1 - Candidato A")
print("2 - Candidato B")
print("3 - Candidato C")
print("0 - Encerrar votação")

# Loop de votação
while True:
    escolha = input("Digite o número do seu voto (ou 0 para encerrar): ")

    if escolha == '0':
        print("\nVotação encerrada!")
        break
    elif escolha in votos:
        votos[escolha] += 1
        print("✅ Voto registrado com sucesso!\n")
    else:
        print("❌ Opção inválida. Tente novamente.\n")

# Exibindo os resultados
print("\n=== Resultado Final ===")
print(f"Candidato A: {votos['1']} voto(s)")
print(f"Candidato B: {votos['2']} voto(s)")
print(f"Candidato C: {votos['3']} voto(s)")
