numero = int(input('Digite um número: '))
contador = 1  # Começa do 1

while contador <= 10:
    resultado = numero * contador
    print(f'{numero} x {contador} = {resultado}')
    contador += 1  # Incrementa o contador
