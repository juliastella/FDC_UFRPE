def encontrar_numero_alterado(quadrado):
    n = len(quadrado)
    soma_esperada = sum(range(1, n+1))

    # Verificar linhas
    for linha in quadrado:
        soma_atual = sum(linha)
        if soma_atual != soma_esperada:
            numero_original = soma_esperada - soma_atual + linha[linha.index(min(linha))]
            numero_alterado = min(linha)
            return numero_original, numero_alterado

    # Verificar colunas
    for coluna in zip(*quadrado):
        soma_atual = sum(coluna)
        if soma_atual != soma_esperada:
            numero_original = soma_esperada - soma_atual + coluna[coluna.index(min(coluna))]
            numero_alterado = min(coluna)
            return numero_original, numero_alterado

# Ler a dimensão do quadrado
N = int(input())

# Ler o quadrado
quadrado = []
for _ in range(N):
    linha = list(map(int, input().split()))
    quadrado.append(linha)

# Chamar a função para encontrar o número alterado
numero_original, numero_alterado = encontrar_numero_alterado(quadrado)

# Imprimir o resultado
print(numero_original, numero_alterado)
