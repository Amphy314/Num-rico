# Autor: @darth_ampharos_ 23/06/2022

import time
start_time = time.time()

def bisection (f, a, b, n = 0, tol = 1.0e-14): 
    # Testando se um dos pontos escolhidoss é solução para a função
    if abs(f(a)) < tol:
            return a
    if abs(f(b)) < tol:
            return b
    
    #Testando se o intervalo escolhido possui dois valores de sinais diferentes
    if f(a)*f(b) > 0:
        print("Erro de intervalo")
        return None
    #Criterio de parada: o método irá se repitir até que o intervalo entre a e b for menor que a tolerancia
    while abs(b-a) > tol:
        #Para x é atribuido o valor da média entre os pontos iniciais
        x = (a+b)/2
        n += 1 
        print(n)
        print(x)
        #Algorítimo checa em qual intervalo a função cruza o eixo x e atualiza o valor de a ou b
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        #end else if          

    return x

def f(x, n, c):
    return (x**n) - c

def raiz_bisecao(n,c):
    def g(x):
        return f(x,n,c)
    #end
    return bisection(g,0,c+1)
#end

