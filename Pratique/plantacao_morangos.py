# Pegar os valores
# Calcular individualmente 
# Compara os valor
# Mostra o resultado

def melhorArea(larguraA, comprimentoA, larguraB, comprimentoB):
  while True:
    area1 = (larguraA * comprimentoA)
    area2 = (larguraB * comprimentoB)

    if area1 > area2:
      return area1
    else:
      return area2


largura1 = int(input("Digite número: "))
comprimento1 = int(input("Digite número: "))
largura2 = int(input("Digite número: "))
comprimento2 = int(input("Digite número: "))

print(melhorArea(largura1, comprimento1, largura2, comprimento2))