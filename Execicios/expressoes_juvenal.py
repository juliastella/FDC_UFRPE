def verifica_bem_definida(cadeia):
    pilha = []
    for caractere in cadeia:
        if caractere in ['{', '[', '(']:
            pilha.append(caractere)
        elif caractere in ['}', ']', ')']:
            if not pilha:
                return False
            topo = pilha.pop()
            if caractere == '}' and topo != '{':
                return False
            elif caractere == ']' and topo != '[':
                return False
            elif caractere == ')' and topo != '(':
                return False
    return not pilha

# Ler o número de instâncias
T = int(input())

# Para cada instância, verificar se a cadeia é bem definida
for _ in range(T):
    cadeia = input().strip()
    if verifica_bem_definida(cadeia):
        print('S')
    else:
        print('N')
