dicionario = {
    'Aluno1': {
        'Nome': 'Raama',
        'Nota': 10,
        'Matematica': 9
    },
    'Aluno2': {
        'Nome': 'Carlos',
        'Nota': 9,
        'Portugues': 8
    }
}

# Calculando a média das notas
total_notas = 0
quantidade_notas = 0

for aluno in dicionario.values():
    for chave, valor in aluno.items():
        if isinstance(valor, (int, float)):  # Só soma os valores numéricos
            total_notas += valor
            quantidade_notas += 1

media = total_notas / quantidade_notas

# Exibindo a média
print(f"Média das notas: {media:.2f}")


