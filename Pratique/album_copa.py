n = int(input())
m = int(input())

figurinhas_compradas = []

for _ in range(m):
    x = int(input())

    if x not in figurinhas_compradas:
        figurinhas_compradas.append(x)

figurinhas_faltam = n - len(figurinhas_compradas)

print(figurinhas_faltam)
