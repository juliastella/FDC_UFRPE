N = int(input())

lampadaA = 0
lampadaB = 0

for i in range(N):
    interruptor = int(input())
    
    if interruptor == 1:
        lampadaA = 1 - lampadaA  # Alternar entre 0 e 1 para lampadaA
    elif interruptor == 2:
        lampadaA = 1 - lampadaA  # Alternar entre 0 e 1 para lampadaA
        lampadaB = 1 - lampadaB  # Alternar entre 0 e 1 para lampadaB

print(lampadaA)
print(lampadaB)
