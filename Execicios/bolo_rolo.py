def tamanho_maximo_fatia(N, K , bolos):
   bolos.sort()
   inicio = 1
   fim = bolos[-1]
   resposta = 0

   while inicio <= fim:
       meio = (inicio + fim) // 2
       total_fatias = sum(b // meio for b in bolos)

       if total_fatias >= N:
           resposta = meio
           inicio = meio + 1
       else:
           fim = meio - 1

   return resposta


N = int(input())
K = int(input())
bolos = list(map(int, input().split()))


resultado = tamanho_maximo_fatia(N, K, bolos)
print(resultado)
