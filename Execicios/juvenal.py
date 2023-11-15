def g(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + g(n/2)
    else:
        return 1 + g(3*n+1)

def maior_valor(a, b): 
 maior = 0

 for numero in range(a, b+1):
    valor = g(numero)
    if valor > maior:
        maior = valor
    else:
       maior = maior
       
 return maior

def caso_de_teste(qtd_testes):
 for testes in range(1, qtd_testes + 1):
    a = int(input())
    b = int(input())
    print(f"Teste {testes}: {maior_valor(a, b)}")

qtd_testes = int(input())
caso_de_teste(qtd_testes)


