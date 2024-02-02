def bfs(tabuleiro, i, j):
    N, M = len(tabuleiro), len(tabuleiro[0])
    ovelhas = 0
    lobos = 0
    visitados = [[False] * M for _ in range(N)]
    fila = [(i, j)]
    visitados[i][j] = True
    while fila:
        x, y = fila.pop(0)
        if tabuleiro[x][y] == 'k':
            ovelhas += 1
        elif tabuleiro[x][y] == 'v':
            lobos += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visitados[nx][ny] and tabuleiro[nx][ny] != '#':
                fila.append((nx, ny))
                visitados[nx][ny] = True
    return ovelhas, lobos

N, M = map(int, input().split())
tabuleiro = [list(input()) for _ in range(N)]
ovelhas_vivas = 0
lobos_vivos = 0

for i in range(N):
    for j in range(M):
        if tabuleiro[i][j] != '#':
            ovelhas, lobos = bfs(tabuleiro, i, j)
            ovelhas_vivas += ovelhas
            lobos_vivos += lobos

print(ovelhas_vivas, lobos_vivos)
