def quantidade(numero):
    lista = list(range(1, numero + 1))
    return lista

def somaLista(lista):
    soma = 0
    
    for elemento in lista:
        soma += elemento
    return soma

numeropecas = int(input())

listaIncompleta = [int(i) for i in input().split()]

somaIncompleta = somaLista(listaIncompleta)
somaCompleta = somaLista(quantidade(numeropecas))

pecaPerdida = somaCompleta - somaIncompleta

print(pecaPerdida)
