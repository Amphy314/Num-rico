import numpy as np
from sl import eliminacao_gaussiana
import time
start_time = time.time()


x = [1.0 ,1.5 ,2.0]
y = [0.0, 0.405465108108164,  0.693147180559945]

def int_pol(x, y):
    q = len(x)
    Q = np.zeros((q, q+1))
    for i in range(q):
        Q[i][q] = y[i]
      
    for i in range(q):
        for j in range(q):
            Q[i][j] = x[i]**j
    return Q
def pol_coef(x, y): 
    print(int_pol(x, y), "\n\n\n")
    P = eliminacao_gaussiana(int_pol(x, y))
    for i in range(len(P)):
        print(P[i],"X ^",i)
pol_coef(x, y)
print("\n======>",time.time()-start_time,"<====== segundos")