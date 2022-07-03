def secante(f, a, b,n=0,N=150):
#Checando se os pontos escolhidos retornam valores com sinais opostos
    if f(a)*f(b) > 0:
        print("Erro de intervalo")
        return None
    for i in range(N):
        n += 1
        #Aplicando o método e atualizando o valor de x
        x = a - f(a)*(b-a)/(f(b)-f(a))
        fx = f(x)
        #Algorítimo checa em qual intervalo a função cruza o eixo x e atualiza o valor de a ou b
        if f(a)*fx < 0:
            b = x
        else:
            a = x
        print(n)
        print(x)
           
    return x

def f(x, n, c):
    return (x**n) - c

def raiz_secante(n,c):
    def g(x):
        return f(x,n,c)
    #end
    return secante(g,0,c+1)

