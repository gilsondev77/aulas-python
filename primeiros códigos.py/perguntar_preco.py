produto1 = float(input('Qual o preço do primeiro produto: '))
produto2 = float(input('Qual o preço do segundo produto: '))
produto3 = float(input('Qual o preço do terceiro produto: '))

menor = min(produto1, produto2, produto3)

print(f'O mais barato é: {menor:.2f}')