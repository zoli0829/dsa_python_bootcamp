def countdown(n):
    print(n)
    if n == 0:
        return 0
    else:
        return countdown(n-1)


countdown(10)

def fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return fibonacci(idx-1) + fibonacci(idx-2)
    

print(fibonacci(3))