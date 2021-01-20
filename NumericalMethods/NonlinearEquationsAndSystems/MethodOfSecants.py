import math

def f(x):
    return (x**2)*math.cos(2*x) + 1


def secant(f, x0, x1, eps):
    fx0 = f(x0)
    fx1 = f(x1)
    for _ in range(1000000000000):
        if abs(fx1) < eps:
            return x1
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
        x0, x1 = x1, x2
        fx0, fx1 = fx1, f(x2)
    return 0


eps = 1e-5
a = 1
b = 6
mylist1 = []
mylist2 = []
k= 1000000
var1 = 0
while a+var1*(5/k) <=b:
 if f(a+var1*(5/k))>f(a+(var1+1)*(5/k)):
   mylist1.append(a + var1 * (5 / k))
   while f(a+var1*(5/k))>f(a+(var1+1)*(5/k)) and a+(var1+1)*(5/k)<=6:
       var1+=1
   mylist2.append(a + var1 * (5 / k))
 else:
    mylist1.append(a + var1 * (5 / k))
    while f(a + var1 * (5 / k)) < f(a + (var1 + 1) * (5 / k)) and a + (var1 + 1) * (5 / k) <= 6:
        var1 += 1
    mylist2.append(a + var1 * (5 / k))
 if 1+var1*(5/k)==b:
     var1+=1


for i in range(len(mylist1)):
 a=mylist1[i]
 b=mylist2[i]
 x = secant(f, mylist1[i], mylist2[i], eps)
 print(str(i+1)+")" + " x = ", end='')
 print(x)
 print("Похибка: ", end='')
 print(f(x))

