from math import sqrt
import string
import sys

#cuadratica
print('cuadratica, variables necesarias a, b, c:')
coxsquare = 0
cox = 0
singleNumber = 0
formSquare = 0

result1 = 0
result2 = 0

def getVar():
    global coxsquare
    coxsquare = int(input('type square x coeficent'))
    global cox
    cox = int(input('type x coeficent'))
    global singleNumber
    singleNumber = int(input('type single number'))


getVar()

if(coxsquare == 0):
    print('The square X coeficent cant be 0')
    getVar()

a = coxsquare
b = cox
c = singleNumber
squareB = b**2



if(squareB >= 4*a*c):
    formSquare = sqrt((b**2)-(4*a*c))
else:
    print(squareB)
    print(4*a*c)
    print('negative squareroot')
    sys.exit()



result1 = (b*(-1)+(formSquare))/(2*a)
result2 = (b*(-1)-(formSquare))/(2*a)

print(result1, ' = x1 ')
print(result2, ' = x2 ')



