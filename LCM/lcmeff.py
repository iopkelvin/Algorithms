# Uses python3
x,y = input().split()
x = int(x)
y = int(y)

def gcd_eff(x,y):
    a = x if (x >= y) else y
    b = x if (x <= y) else y
    while b != 0:
        a, b = b, a%b
    return a

def lcm_eff(x,y):
    return (x*y)//gcd_eff(x,y)

print(lcm_eff(x,y))
