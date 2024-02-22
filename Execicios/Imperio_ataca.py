def esta_na_regiao(planeta, planos):
    regioes = []
    for plano in planos:
        if plano[0]*planeta[0] + plano[1]*planeta[1] + plano[2]*planeta[2] == plano[3]:
            regioes.append(True)
        else:
            regioes.append(False)
    return tuple(regioes)

M, N = map(int, input().split())
planos = [list(map(int, input().split())) for _ in range(M)]
planetas = [list(map(int, input().split())) for _ in range(N)]

contagem_regioes = {}
for planeta in planetas:
    regiao = tuple(esta_na_regiao(planeta, planos))
    if regiao not in contagem_regioes:
        contagem_regioes[regiao] = 0
    contagem_regioes[regiao] += 1

maximo = max(contagem_regioes.values())

print(maximo)
