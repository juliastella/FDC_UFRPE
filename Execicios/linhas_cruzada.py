def mesclar_e_contar_cruzamentos(esquerda, direita):
    mesclada = []
    cruzamentos = 0
    i, j = 0, 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            mesclada.append(esquerda[i])
            i += 1
        else:
            mesclada.append(direita[j])
            cruzamentos += len(esquerda) - i
            j += 1

    mesclada.extend(esquerda[i:])
    mesclada.extend(direita[j:])
    return mesclada, cruzamentos

def merge_sort_e_contar_cruzamentos(lista):
    if len(lista) <= 1:
        return lista, 0

    meio = len(lista) // 2
    esquerda, cruzamentos_esquerda = merge_sort_e_contar_cruzamentos(lista[:meio])
    direita, cruzamentos_direita = merge_sort_e_contar_cruzamentos(lista[meio:])
    mesclada, cruzamentos_mesclagem = mesclar_e_contar_cruzamentos(esquerda, direita)

    total_cruzamentos = cruzamentos_esquerda + cruzamentos_direita + cruzamentos_mesclagem
    return mesclada, total_cruzamentos

def contar_cruzamentos(n, ordem):
    _, cruzamentos = merge_sort_e_contar_cruzamentos(ordem)
    return cruzamentos

n = int(input())
ordem = list(map(int, input().split()))

resultado = contar_cruzamentos(n, ordem)
print(resultado)
