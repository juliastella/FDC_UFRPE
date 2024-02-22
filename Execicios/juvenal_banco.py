def processar_comandos(t):
    casos = [[]]
    condicional = False

    for i in range(t):
        if  1 > t or t >  1000:
            condicional = True
            break
        n = int(input())
        if n <  1 or n >  1000:
            condicional = True
            break

        fila_regular = []
        fila_preferencial = []
        casos += [[]]

        for j in range(n):
            entrada = list(map(str, input().split()))
            if len(entrada) >  1:  
                if int(entrada[1]) <  1 or int(entrada[1]) >  100:
                    condicional = True
                    break

            if entrada[0] == "f":
                fila_regular.append(entrada[1])
            elif entrada[0] == "p":
                fila_preferencial.append(entrada[1])
            elif entrada[0] == "I":
                if fila_regular and fila_preferencial:
                    casos[i].append((fila_regular[0], fila_preferencial[0]))
                elif fila_regular and not fila_preferencial:
                    casos[i].append((fila_regular[0],"0"))
                elif not fila_regular and fila_preferencial:
                    casos[i].append(("0", fila_preferencial[0]))
                elif not fila_regular and not fila_preferencial:
                    casos[i].append(("0","0"))
            elif fila_regular and entrada[0] == "A":
                fila_regular.pop(0)
            elif not fila_regular and entrada[0] == "A":
                fila_preferencial.pop(0)
            elif fila_preferencial and entrada[0] == "B":
                fila_preferencial.pop(0)
            elif not fila_preferencial and entrada[0] == "B":
                fila_regular.pop(0)
        if condicional:
            break

    if casos[0]:
        for m in range(len(casos)-1):
            print("Caso "+ str(m+1) + ":" )
            for n in range(len(casos[m])):
                print(casos[m][n][0], casos[m][n][1])

# Ler o número de casos de teste
t = int(input())
processar_comandos(t)
