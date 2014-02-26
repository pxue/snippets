
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    if n == 0: return 0
    f = [0, 1]
    for i in xrange(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

print fibonacci2(5)
    




