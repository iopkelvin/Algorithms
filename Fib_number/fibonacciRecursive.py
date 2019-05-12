# Uses python3
import numpy as np
def fib_list(n):
    #while n>=0 and n<=45:
    a=0
    b=1
    for i in range(n):
        a,b= b, a+b
        print(a,b)
    return a
    '''  F = np.array([0, 1])
        for i in range(2,n+1):
            K = F[i-1] + F[i-2]
            F = np.append(F,K)
        return F[n]
'''
n = int(input())
print(fib_list(n))
