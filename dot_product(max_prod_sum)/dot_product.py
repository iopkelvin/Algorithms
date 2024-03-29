#Uses python3

import sys

def max_dot_product(a,b):
    A = sorted(a, reverse=True)
    B = sorted(b, reverse=True)
    sums = 0
    for i,j in zip(A,B):
        mult = i*j
        sums += mult
    return sums

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
