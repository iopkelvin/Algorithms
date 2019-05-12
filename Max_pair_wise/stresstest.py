def max_pairwise_product_fast(numbers):
    index1 = 0
    n = len(numbers)
    for i in range(1, n):
        if numbers[i] > numbers[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for i in range(0, n):
        if (i != index1) and (numbers[i] > numbers[index2]):
            index2 = i
    print(index1, index2)
    return (numbers[index1] * numbers[index2])

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product




def stress_test(N, M):
    import numpy as np
    while True:
        n = np.random.randint(2,N)
        A = np.random.randint(0,M,n)
        for i in range(0,n):
            A[i] = np.random.randint(0,M)
        print(A)
        result1 = max_pairwise_product(A)
        result2 = max_pairwise_product_fast(A)
        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer:", result1, result2)
            break

if __name__ == '__main__':
    input_N = int(input())
    input_M = int(input())
    print(stress_test(input_N, input_M))
