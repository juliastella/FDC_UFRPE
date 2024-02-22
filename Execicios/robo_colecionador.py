def coletar_figurinhas(arena, N, M, S, instrucoes):
    # Inicializar posição inicial do robô
    for i in range(N):
        for j in range(M):
            if arena[i][j] in ['N', 'S', 'L', 'O']:
                direcao = arena[i][j]
                posicao = (i, j)
                arena[i][j] = '.'  # remover o robô da arena
                break

    # Inicializar variáveis
    dx = {'N': -1, 'S': 1, 'L': 0, 'O': 0}  # Movimento vertical
    dy = {'N': 0, 'S': 0, 'L': 1, 'O': -1}  # Movimento horizontal
    figurinhas_coletadas = 0

    # Simular o movimento do robô
    for instrucao in instrucoes:
        if instrucao == 'F':
            novo_x = posicao[0] + dx[direcao]
            novo_y = posicao[1] + dy[direcao]
            
            # Verificar se o movimento é válido
            if 0 <= novo_x < N and 0 <= novo_y < M and arena[novo_x][novo_y] != '#':
                posicao = (novo_x, novo_y)
                if arena[novo_x][novo_y] == '*':
                    figurinhas_coletadas += 1
        elif instrucao == 'D':
            if direcao == 'N':
                direcao = 'L'
            elif direcao == 'L':
                direcao = 'S'
            elif direcao == 'S':
                direcao = 'O'
            elif direcao == 'O':
                direcao = 'N'
        elif instrucao == 'E':
            if direcao == 'N':
                direcao = 'O'
            elif direcao == 'O':
                direcao = 'S'
            elif direcao == 'S':
                direcao = 'L'
            elif direcao == 'L':
                direcao = 'N'

    return figurinhas_coletadas

# Ler a entrada
while True:
    N, M, S = map(int, input().split())
    if N == M == S == 0:
        break
    arena = [list(input()) for _ in range(N)]
    instrucoes = input()

    # Executar a simulação e imprimir o resultado
    resultado = coletar_figurinhas(arena, N, M, S, instrucoes)
    print(resultado)
