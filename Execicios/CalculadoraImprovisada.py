def sucessor(a):
    return a + 1

def soma(a, b):
  for _ in range(b):
    a = sucessor(a)
  return a

def multiplicacao(a, b):
  c = 0
  for _ in range(b):
    c = soma(c, a)
  return c

def exponenciacao(a, b):
  c = 1
  for _ in range(b):
    c = multiplicacao(c, a)
  return c

while True:
    operacao = input().split()

    if operacao[0] == "Suc":
        a = int(operacao[1])
        resultado = sucessor(a)
        print(resultado)

    elif operacao[0] == "Soma":
        a = int(operacao[1])
        b = int(operacao[2])
        resultado = soma(a, b)
        print(resultado)

    elif operacao[0] == "Mult":
        a = int(operacao[1])
        b = int(operacao[2])
        resultado = multiplicacao(a, b)
        print(resultado)

    elif operacao[0] == "Exp":
        a = int(operacao[1])
        b = int(operacao[2])
        resultado = exponenciacao(a, b)
        print(resultado)

    else:
        break

