
from math import sqrt


def cuadratic(a, b, c):
    result = []
    if(a == 0):
        print('a cant be zero')
        return
    if(b**2 < 4*a*c):
        print('negative squareroot error')
        return
    result.append(((b*(-1)+(sqrt((b**2)-(4*a*c))))/(2*a)))
    result.append(((b*(-1)-(sqrt((b**2)-(4*a*c))))/(2*a)))
    return result

print(cuadratic(12,6,-3))