retangulo1 = [int(i) for i in input().split()]
retangulo2 = [int(i) for i in input().split()]

if retangulo1[0] > retangulo2[2] or retangulo1[2] < retangulo2[0]:
  print("0")
elif retangulo1[1] > retangulo2[3] or retangulo1[3] < retangulo2[1]:
  print("0")
else:
  print("1")
