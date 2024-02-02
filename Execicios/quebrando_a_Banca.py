def encontrar_maior_saldo(A, B, saldo):
   saldo_lista = list(map(int, saldo))
   saldo_ordenado = sorted(saldo_lista, reverse=True)
   if B > len(saldo_ordenado):
       B = len(saldo_ordenado)
   saldo_final = saldo_ordenado[:-B]
   return ''.join(map(str, saldo_final))

while True:
   entrada = input().split()
   if len(entrada) == 0:
       break
   A, B = map(int, entrada)
   saldo = input()
   
   resultado = encontrar_maior_saldo(A, B, saldo)

   print(resultado)
