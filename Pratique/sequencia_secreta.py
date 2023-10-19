# Leia o tamanho da sequência
N = int(input())

# Inicialize as variáveis
max_marcados = 1  # Inicialmente, pelo menos um número pode ser marcado
contador = 1
anterior = int(input())  # Leia o primeiro número

# Leia a sequência de números
for _ in range(1, N):
    sequencia = int(input())
    
    # Verifique se o número atual é igual ao anterior
    if sequencia == anterior:
        contador = 1
    else:
        contador += 1
    
    # Atualize o número máximo de números marcados
    max_marcados = contador
    
    # Atualize o valor anterior
    anterior = sequencia

# Imprima o valor máximo de números marcados
print(max_marcados)
