import sys
import time 
from Newton import raiz_newton
from bisection_method import raiz_bisecao
from Secante import raiz_secante
start_time = time.time()

n = float(sys.argv[2])
c = float(sys.argv[3])

if sys.argv[1] == "raiz_newton":
    raiz_newton(n,c)
if sys.argv[1] == "raiz_bisecao":
    raiz_bisecao(n,c)
if sys.argv[1] == "raiz_secante":
    raiz_secante(n, c)

# no segundo argumento escolha: raiz_newton ou raiz_bisecao 
# no terceiro e quarto escolha o índice e valor a ser radiciado
# no ultimo escolha um chute inicial 

print("\n\n----%s segundos----" % (time.time() - start_time))