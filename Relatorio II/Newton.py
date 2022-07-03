def newton(f,Df,x0,tol = 1.0e-14, max_iter = 100):
    xn = x0
    n = 0
    while abs(f(xn)) > tol:
        #Associando f(xn) e Df(xn) a duas variavies
        n += 1
        fxn = f(xn)
        Dfxn = Df(xn)
        #Aplicando o método e atualizando o valor de xn
        xn = xn - fxn/Dfxn
        print(xn)
        if n == max_iter:
            # Método de parada secundário baseado em número de interações
            print("resultado com erro maior que a tolerancia")
            return xn
    return xn   

def f(x,n,c):
    return (x**n) - c

def Df(x,n,c):
    return n*(x**(n-1))

def raiz_newton(n,c):
    def g(x):
        return f(x,n,c)
    def Dg(x):
        return Df(x, n, c)  
    return newton(g, Dg, 1)


