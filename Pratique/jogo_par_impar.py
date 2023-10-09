p = int(input('Digiti 0 ou 1: '))
d1 = int(input('Digiti a quantidade dedos: '))
d2 = int(input('Digiti a quantidade dedos: '))

def impar_par(numero1, numero2):
  if (numero1 + numero2)% 2 == 1:
    return('impar')
  else:
    return('par')
  

if (p == 0 and impar_par(d1,d2) == 'par'):
  print(0)
elif (p == 0 and impar_par(d1,d2) == 'impar'):
  print(1)
elif (p == 1 and impar_par(d1,d2) == 'par'):
  print(1)
elif (p == 1 and impar_par(d1,d2) == 'impar'):
  print(0)