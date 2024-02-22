# Ler a dimensão do quadrado
dimensao_quadrado = int(input("Digite a dimensão do quadrado: "))

# Ler o quadrado
matriz_quadrado = [[int(valor) for valor in input("Digite os números da linha " + str(y +  1) + " separados por espaço: ").split()] for y in range(dimensao_quadrado)]

# Calcular a segunda menor soma sem usar sum ou min
somas_linhas = [sum(linha) for linha in matriz_quadrado]
segunda_menor_soma = min(somas_linhas[1:])

# Encontrar a linha onde a soma não é igual à segunda menor soma
indice_linha_alterada = next(i for i, soma in enumerate(somas_linhas) if soma != segunda_menor_soma)

# Encontrar a coluna onde a soma não é igual à segunda menor soma
somas_colunas = [sum(linha[i] for linha in matriz_quadrado) for i in range(dimensao_quadrado)]
indice_coluna_alterada = next(i for i, soma in enumerate(somas_colunas) if soma != segunda_menor_soma)

# Imprimir os resultados
numero_alterado = matriz_quadrado[indice_linha_alterada][indice_coluna_alterada]
numero_original = segunda_menor_soma - (somas_linhas[indice_linha_alterada] - numero_alterado)
print(numero_original, numero_alterado)
