import numpy as np
def calc_fib(n):
    if n <= 1:
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)

def fib_list(n):
    #while n>=0 and n<=45:
    a=0
    b=1
    for i in range(n):
        a,b= b, a+b
    return a


def testing(N,M):
    while True:
        n = np.random.randint(2,N)
        A = np.random.randint(0,M,n)
        for i in range(0,n):
            A[i] = np.random.randint(0,M)
        print(A)
        result1 = int(calc_fib(A))
        result2 = int(fib_list(A))
        if (result1 == result2):
            print("Ok")
        else:
            print("Wrong answer:", result1, result2)
            break

if __name__ == "__main__":
    input_N = int(input())
    input_M = int(input())
    print(testing(input_N, input_M))
