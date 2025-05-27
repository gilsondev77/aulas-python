def verificar_chaves(dicionario, lista_chaves):
    return all(chave in dicionario for chave in lista_chaves)

# Criando um dicionário correto
dicionario = {
    'Carro': 'Azul',
    'Casa': 'Branca',
    'Moto': 'Preta',
    'Bicicleta': 'Vermelha'
}

# Lista de chaves para verificar
chaves_para_verificar = ['Carro', 'Casa', 'Bicicleta']

# Verificando
resultado = verificar_chaves(dicionario, chaves_para_verificar)

# Mostrando o resultado
print("Todas as chaves existem?", resultado)

