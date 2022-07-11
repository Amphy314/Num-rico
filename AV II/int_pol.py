import numpy as np
from sl import eliminacao_gaussiana
import time
start_time = time.time()

# e^(-1/x^2) de 1 a 2:
x = [1.0 ,1.5 ,2.0]
y = [0.36787944117144233, 0.641180388429954582251520479131204482604147,  0.7788007830714]

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