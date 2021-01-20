import math
import decimal

# Функція
def F(x):
    pi = 2**x - 4*x
    return pi

# Похідна
def F1(x):
    pi = 2 ** x * math.log(2, math.e) - 4
    return pi
    pi =2**x * math.log(x, math.e) - 4
    return pi


def Method(a, b):
        x0 = (a + b) / 2
        xn = F(x0)
        xn1 = xn - F(xn) / F1(xn)
        while abs(xn1 - xn) > math.pow(10, -5):
            xn = (xn1)  # вот так надо было
            xn1 = xn - F(xn) / F1(xn)
        #print(xn1)
        return xn1


a = -10
b = 10
result1= Method(a,b)
for i in range(a,b+1):
   result2 = Method(i,i)
   if int(result1) != int(result2):
       break
print(result1)
print(result2)

