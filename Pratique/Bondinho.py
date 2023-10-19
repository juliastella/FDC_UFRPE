a = int(input())
b = int(input())

def quantidade(a, b):
    
    c = a + b

    if (c > 50):
        print('N')
    else:
        print('S')
    
print(quantidade(a, b))