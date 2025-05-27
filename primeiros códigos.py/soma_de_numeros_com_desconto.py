total = 0

for i in range(5):  # Loop para inserir 5 preços
    preco = float(input(f"Digite o preço do produto {i + 1}: "))
    total += preco  # Soma o preço ao total
    
    if total > 100:  # Verifica se o total ultrapassou 100
        desconto = total * 0.10
        total -= desconto
        print(f"Total ultrapassou 100. Desconto de 10% aplicado: R$ {desconto:.2f}")
        break  # Interrompe o loop

print(f"Total final: R$ {total:.2f}")



