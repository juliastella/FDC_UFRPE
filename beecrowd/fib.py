# Dicionário para armazenar os valores de Fibonacci já calculados
fib_cache = {}

def fib(x):
    # Verificar se o valor já está em cache
    if x in fib_cache:
        return fib_cache[x]

    # Calcular o valor de Fibonacci
    if x == 0:
        fib_cache[x] = (0, 0)
    elif x == 1:
        fib_cache[x] = (1, 0)
    else:
        fib1, calls1 = fib(x-1)
        fib2, calls2 = fib(x-2)
        fib_cache[x] = (fib1 + fib2, calls1 + calls2 + 2)

    return fib_cache[x]

n = int(input())

for _ in range(n):
    x = int(input())
    fib_result, num_calls = fib(x)
    print(f"fib({x}) = {num_calls} calls = {fib_result}")
