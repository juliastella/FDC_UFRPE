def menor_pastas(N, B, tamanhos):
 tamanhos.sort(reverse=True)

 pastas = [[]]

 # Para cada arquivo
 for i in range(N):
     for j in range(len(pastas)):
         total = 0
         for k in pastas[j]:
             total += k
         if total + tamanhos[i] <= B:
             pastas[j].append(tamanhos[i])
             break
     else:
         pastas.append([tamanhos[i]])

 return len(pastas)


N = int(input())
B = int(input())
tamanhos = []
for i in range(N):
   tamanhos.append(int(input()))


print(menor_pastas(N, B, tamanhos))
