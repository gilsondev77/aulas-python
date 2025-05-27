# Solicita ao usuário o preço do produto e a quantidade comprada
preco_do_produto = float(input('Digite o preço do produto: '))
quantidade_comprada = int(input('Digite a quantidade comprada: '))

# Calcula o total inicial
total = preco_do_produto * quantidade_comprada

# Verifica se há desconto
if quantidade_comprada > 10:
    desconto = total * 0.10  # Calcula o desconto de 10%
    total -= desconto  # Aplica o desconto
    print(f"Desconto aplicado: R${desconto:.2f}")
else:
    print("Não há desconto.")

# Exibe o valor total final
print(f"Valor total a pagar: R${total:.2f}")
