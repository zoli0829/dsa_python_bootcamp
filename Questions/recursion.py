def findSum(n):
    if n == 1:
        return 1
    else:
        return n + findSum(n - 1)


print(findSum(5))


def countdown(n):
    print(n)
    if n < 0:
        print("Please enter a postive number!")
    elif n == 0:
        return
    else:
        countdown(n-1)


countdown(3)


def fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return fibonacci(idx-1) + fibonacci(idx-2)
    

print(fibonacci(8))