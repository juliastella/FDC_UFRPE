def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) ==  0:
        return len(s1)

    previous_row = range(len(s2) +  1)
    for i, c1 in enumerate(s1):
        current_row = [i +  1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j +  1] +  1
            deletions = current_row[j] +  1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# Ler o número de palavras no dicionário e as palavras fornecidas pelo usuário
num_palavras_dicionario, num_palavras_usuario = map(int, input().split())
dicionario = [input().strip() for _ in range(num_palavras_dicionario)]
palavras_usuario = [input().strip() for _ in range(num_palavras_usuario)]

# Para cada palavra fornecida pelo usuário, encontrar palavras no dicionário que são similares
for palavra_usuario in palavras_usuario:
    palavras_similares = []
    for palavra_dicionario in dicionario:
        distancia = levenshtein(palavra_usuario, palavra_dicionario)
        if distancia <=  2:
            palavras_similares.append(palavra_dicionario)
    print(' '.join(palavras_similares) if palavras_similares else '')
