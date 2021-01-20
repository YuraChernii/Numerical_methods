import numpy as np
import matplotlib.pyplot as plt


x=np.array([6.5, 7.7, 8.2, 6.2, 7.4], dtype=float)
y=np.array([2.698, 3.004, 3.123, 2.618, 2.930], dtype=float)


def lagranz(x,y,t):
         z=0
         for j in range(len(y)):
             p1=1; p2=1
             for i in range(len(x)):
                 if i==j:
                     p1=p1*1; p2=p2*1
                 else:
                     p1=p1*(t-x[i])
                     p2=p2*(x[j]-x[i])
             z=z+y[j]*p1/p2
         return z


steps = int(input("Enter steps:"))
xnew =[]
h=(np.max(x)-np.min(x))/float(steps)
for i in range(steps+1):
    xnew.append(np.min(x)+i*h)
ynew=[]
for i in xnew:
    ynew.append(lagranz(x,y,i))
plt.plot(x,y,'o',xnew,ynew)
plt.show()


#For sin() func:
#import numpy as np
#import math
#import matplotlib.pyplot as plt
#
#
#def lagranz(x,y,t):
#         z=0
#         for j in range(len(y)):
#             p1=1; p2=1
#             for i in range(len(x)):
#                 if i==j:
#                     p1=p1*1; p2=p2*1
#                 else:
#                     p1=p1*(t-x[i])
#                    p2=p2*(x[j]-x[i])
#             z=z+y[j]*p1/p2
#         return z
#
#
#x1=[]
#y1=[]
#for i in range(1,10):
#    x1.append(i*0.4)
#    y1.append(math.sin(i*0.4))
#steps = int(input("Enter steps:"))
#xnew =[]
#h=(np.max(x1)-np.min(x1))/float(steps)
#for i in range(steps+1):
#    xnew.append(np.min(x1)+i*h)
#ynew=[]
#for i in xnew:
#    ynew.append(lagranz(x1,y1,i))
#plt.plot(x1,y1,'o',xnew,ynew)
#plt.show()
