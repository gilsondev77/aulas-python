informacoes_pessoais = [
    {'Nome': 'Gil', 'Idade': '33', 'Cidade': 'São Paulo'},
    {'Nome': 'Ana', 'Idade': '29', 'Cidade': 'Rio de Janeiro'}
]

print("Informações Pessoais:")
for pessoa in informacoes_pessoais:
    print(f"Nome: {pessoa['Nome']}")
    print(f"Idade: {pessoa['Idade']}")
    print(f"Cidade: {pessoa['Cidade']}")
    print()
