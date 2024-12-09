def pares_ate(n:int):
    for i in range(2, n+1, 2):
        yield i
    
generator = pares_ate(8)
for par in generator:
    print(par)