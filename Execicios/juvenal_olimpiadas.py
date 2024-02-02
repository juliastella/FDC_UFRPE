def classifica_paises():
    N, M = map(int, input().split())
    resultados = {i: [0, 0, 0] for i in range(1, N + 1)}

    for _ in range(M):
        O, P, B = map(int, input().split())
        resultados[O][0] += 1
        resultados[P][1] += 1
        resultados[B][2] += 1

    # Classificação inicial baseada em ouro, depois prata e bronze
    classificacao = list(resultados.keys())

    for _ in range(len(classificacao)):
        for i in range(len(classificacao) - 1):
            # Correção na condição de troca
            if (resultados[classificacao[i]][0] < resultados[classificacao[i + 1]][0]) or \
               (resultados[classificacao[i]][0] == resultados[classificacao[i + 1]][0] and resultados[classificacao[i]][1] < resultados[classificacao[i + 1]][1]) or \
               (resultados[classificacao[i]][0] == resultados[classificacao[i + 1]][0] and resultados[classificacao[i]][1] == resultados[classificacao[i + 1]][1] and resultados[classificacao[i]][2] < resultados[classificacao[i + 1]][2]) or \
               (resultados[classificacao[i]][0] == resultados[classificacao[i + 1]][0] and resultados[classificacao[i]][1] == resultados[classificacao[i + 1]][1] and resultados[classificacao[i]][2] == resultados[classificacao[i + 1]][2] and classificacao[i] > classificacao[i + 1]):
                classificacao[i], classificacao[i + 1] = classificacao[i + 1], classificacao[i]

    # Imprime a classificação
    for id in classificacao:
        print(id, end=' ')

classifica_paises()
