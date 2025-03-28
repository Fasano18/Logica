def rotacionar_direita(lst, k):
    # Se a lista estiver vazia ou se k for 0, retorna a lista como está
    if not lst or k == 0:
        return lst

    # Garante que o k não seja maior que o tamanho da lista
    k = k % len(lst)

    # Faz a rotação pegando os últimos k elementos e colocando no começo da lista
    return lst[-k:] + lst[:-k]


def rotacionar_esquerda(lst, k):
    if not lst or k == 0:
        return lst

    k = k % len(lst)

    return lst[k:] + lst[:k]



# Teste
lista = [1, 2, 3, 4, 5, 6, 7]
k = 2

# Mostra a lista rotacionada
print(rotacionar_direita(lista, k))
print(rotacionar_esquerda(lista, k))
