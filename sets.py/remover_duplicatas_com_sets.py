def remover_duplicatas(lista):
    """
    Remove duplicatas de uma lista usando sets.

    Args:
        lista: A lista original.

    Returns:
        Uma nova lista com duplicatas removidas.
    """
    return list(set(lista))

# Exemplo de uso:
minha_lista = [1, 2, 2, 3, 4, 4, 5]
nova_lista = remover_duplicatas(minha_lista)
print(nova_lista)  # Saída: [1, 2, 3, 4, 5]