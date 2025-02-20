import pdb

def factorial(n):
    pdb.set_trace()
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)