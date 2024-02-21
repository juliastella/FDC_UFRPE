import time

start_time = time.time()

def fib(n):
	if n<=1:
		return n
	else:
		return fib(n-2) + fib(n-1)


  
numb = int(input())   

end_time = time.time()

tempo_execusao = end_time - start_time

print(f'Fib é: {fib(numb)}, o tempo é de {tempo_execusao} segundos')



