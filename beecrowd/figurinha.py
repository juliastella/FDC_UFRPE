def calcular_mdc(a, b):
    while b:
        a, b = b, a % b

    return a

n = int(input())

for _ in range(n):
    entrada = input()
    f1 = ""
    f2 = ""
    i = 0
 # lê o primeiro número até encontrar um espaço
    while entrada[i] != " ":
        f1 += entrada[i]
        i += 1

    i += 1  # pula o espaço

    # lê o segundo número até o final da string
    while i < len(entrada):
        f2 += entrada[i]
        i += 1

    # converte os números de string para int
    f1 = int(f1)
    f2 = int(f2)

    print(calcular_mdc(f1, f2))
