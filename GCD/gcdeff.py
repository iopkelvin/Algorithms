# Uses python3
'''import sys'''

x,y = input().split()
x = int(x)
y = int(y)

def efficient(x, y):
    a = x if (x >= y) else y
    #print(a)
    b = y if (y <= x ) else x
    #print(b)
    while b != 0:
        a,b = b, a%b
        #print(a,b)
    return a

print(efficient(x, y))




'''
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
'''
