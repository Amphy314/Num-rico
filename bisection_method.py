# Autor: @darth_ampharos_ 23/06/2022

import time
start_time = time.time()

def bisection (f, a, b, n = 0, tol = 1.0e-14): 
    
    if abs(f(a)) < tol:
            return a
    if abs(f(b)) < tol:
            return b
    
    if f(a)*f(b) > 0:
        print("Erro de intervalo")
    
    while abs(b-a) > tol:
        x = (a+b)/2
        n += 1 
        print(n)
        print(x)
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        #end else if          

    return x

def f(x):
    return x**5 - 3*x**4 + 2*x**3 - 6*x**2 + 5*x - 3

bisection(f, -6, 6,)
print("\n\n----%s segundos----" % (time.time() - start_time))
