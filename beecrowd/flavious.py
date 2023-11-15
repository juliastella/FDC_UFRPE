def josephus(n, k):
    result = 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result + 1



nc = int(input())

for i in range(1, nc + 1):
    entrada = input()
    n_circulo = ""
    k_tamanho = ""
    j = 0

    while entrada[j] != " ":
        n_circulo += entrada[j]
        j += 1

    j += 1

    while j < len(entrada):
        k_tamanho += entrada[j]
        j += 1

    n_circulo = int(n_circulo)
    k_tamanho = int(k_tamanho)

    sobrevivente = josephus(n_circulo, k_tamanho)
    print(f"Case {i}: {sobrevivente}")

    

