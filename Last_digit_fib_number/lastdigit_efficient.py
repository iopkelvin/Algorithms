# python3
import numpy as np
def fib_list(n):
    a,b = 0,1
    for i in range(n):
        a,b = b%10, a+b % 10
        print(a,b)
    return a

    '''
    F = np.array([0, 1])
    for i in range(2,n+1):
        K = (F[i-1] + F[i-2])%10
        F = np.append(F,K)
        #print(i)
        #print(F)
    return F[n]
    '''
n = int(input())
print(fib_list(n))
