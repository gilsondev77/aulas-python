# Recebendo as duas listas
lista1 = [1, 2, 3, 4, 5, 3]
lista2 = [4, 5, 6, 7, 8, 5]

# Convertendo as listas para conjuntos para obter apenas os elementos únicos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Calculando a união dos conjuntos
uniao = conjunto1.union(conjunto2)

# Exibindo o resultado
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("União dos elementos únicos:", uniao)
