# Função para encontrar o maior saldo possível após remover dígitos
def encontrar_maior_saldo(A, B, saldo):
    saldo_lista = list(map(int, saldo))
    saldo_ordenado = sorted(saldo_lista, reverse=True)
    saldo_final = saldo_ordenado[B:]
    return ''.join(map(str, saldo_final))


# Processar cada caso de teste
while True:
    entrada = input().split()
    if len(entrada) == 0:
        break
    A, B = map(int, entrada)
    saldo = input()
    
    # Chamar a função para encontrar o maior saldo possível
    resultado = encontrar_maior_saldo(A, B, saldo)

    # Imprimir o resultado
    print(resultado)
