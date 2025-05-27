# Criando um conjunto vazio
frutas = set()

# Adicionando as frutas uma por uma
frutas.add("maçã")
frutas.add("banana")
frutas.add("uva")
frutas.add("laranja")
frutas.add("morango")

# Imprimindo o conjunto
print(frutas)

# Verificando se "banana" está presente no conjunto
if "banana" in frutas:
    print("A fruta 'banana' está presente no conjunto.")
else:
    print("A fruta 'banana' NÃO está presente no conjunto.")
