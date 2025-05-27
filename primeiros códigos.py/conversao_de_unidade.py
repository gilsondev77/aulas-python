# Definindo a função para conversão
def metros_para_centimetros(metros):
    return metros * 100

# Obter o valor em metros
metros = float(input('Digite um valor em metros: '))

# Converter metros para centímetros
centimetros = metros_para_centimetros(metros)

# Exibir o resultado
print(f'{metros} metros equivalem a {centimetros} centímetros.')
