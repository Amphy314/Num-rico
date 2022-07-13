import numpy as np
from data import x
from data import y

def cubic_spline(x, y):
    S = np.zeros((len(y),len(y)+1))
    for i in range(len(y)-1):
        S[i][len(x)] = y[i]
    for i in range(len(y)):
        for j in range(len(y)):
            S[i][j] = x[i]
    print(S)

cubic_spline(x, y)   