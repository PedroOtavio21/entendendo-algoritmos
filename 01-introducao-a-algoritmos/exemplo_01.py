def pesquisa_binaria (lista, item):
    inicio = 0 # 1
    fim = len(lista) - 1 # 1

    while inicio <= fim: # 2
        meio = (inicio + fim) // 2 # 3
        chute = lista[meio]

        if chute == item: # 4
            return meio
        if chute < item: # 5
            inicio = meio + 1
        else: # 6
            fim = meio - 1
    return None # 7

minha_lista = [1, 3, 5, 7, 9] # 8

print(pesquisa_binaria(minha_lista, 7)) # 9
print(pesquisa_binaria(minha_lista, 2)) # 10

"""
1. inicio e fim acompanham o escopo da lista que você está procurando.
2. Enquanto ainda não conseguiu chegar a um único elemento ...
3. ... verifica o elemento central
4. Acha o item
5. O chute foi muito alto
6. O chute foi muito baixo
7. O item não existe
8. Teste a lista!
9. Lembrando: As listas começam com 0, e o próximo endereço tem o indice 1
10. "None" significa nulo em Python, indicando que o item não foi encontrado.
"""