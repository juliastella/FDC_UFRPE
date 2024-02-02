N = int(input())
M = int(input())
tabuleiro = []
for i in range(N):
   linha = list(input())
   tabuleiro.append(linha)
K = int(input())
disparos = []
for i in range(K):
   linha = input().split()
   disparo = (int(linha[0]), int(linha[1]))
   disparos.append(disparo)

navios_destruidos = {}
for disparo in disparos:
   if tabuleiro[disparo[0]-1][disparo[1]-1] == '#':
       navios_destruidos[disparo] = 1

total_navios_destruidos = 0
for disparo in navios_destruidos:
   total_navios_destruidos += navios_destruidos[disparo]

print(total_navios_destruidos)
