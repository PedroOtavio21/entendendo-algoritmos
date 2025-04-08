# Algoritmo de ordenação -> menor ao maior

def buscaMenor(arr):
    menor = arr[0] # 1
    menor_indice = 0 # 2
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

# 1 - Armazena o menor valor do array
# 2 - Armazena o índice do menor valor

def ordenacaoPorSelecao(arr): # 1
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) # 2
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))

# 1 - Ordenação em um array
# Encontra o menor elemento do array e adiciona ao novo array.