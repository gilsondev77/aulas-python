def uniao_conjuntos(*conjuntos):
    novo_conjunto = set()
    for conjunto in conjuntos:
        novo_conjunto = novo_conjunto.union(conjunto)
    return novo_conjunto

conjunto_A = (1, 2, 3, 4,)
conjunto_B = ('a', 'b', 'c', 'd')
conjunto_C = ('@', '#', '$', '%')

uniao = uniao_conjuntos(conjunto_A, conjunto_B, conjunto_C)

print(f'A uniao dos conjuntos é: {uniao}')