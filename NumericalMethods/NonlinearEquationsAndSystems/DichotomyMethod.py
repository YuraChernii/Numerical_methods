import math

def f(x):
    return (x**2)*math.cos(2*x) + 1

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
 while abs(b - a) > eps:
    x = (a + b) / 2.0
    fx = f(x)
    fa = f(a)
    if (fx < 0 and fa < fx):
        a = x
        continue
    if(fx > 0 and fa > fx):
        a = x
        continue
    b = x
 print(str(i+1)+")" + " x = ", end='')
 print(x)
 print("Похибка: ", end='')
 print(f(x))

