import math
import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rcParams['font.family'] = 'fantasy'
def mnkGP(x,y):
              n=len(x)
              s=sum(y)
              s1=sum([1/x[i] for i in  range(0,n)]) #  сумма 1/x
              s2=sum([(1/x[i])**2 for i in  range(0,n)]) #  сумма (1/x)**2
              s3=sum([y[i]/x[i]  for i in range(0,n)])  # сумма y/x
              a= round((s*s2-s1*s3)/(n*s2-s1**2),3) # коефіціент a з трьома дробовими цифрами
              b=round((n*s3-s1*s)/(n*s2-s1**2),3)# коефіціент b з трьома дробовими цифрами
              s4=[a+b/x[i] for i in range(0,n)] # список значень гіперболічної функції
              so=round(sum([abs(y[i] -s4[i]) for i in range(0,n)])/(n*sum(y))*100,3)   # середня похибка апроксимації
              plt.title('Апроксимація гіперболою Y='+str(a)+'+'+str(b)+'/x\n середня похибка--'+str(so)+'%',size=14)
              plt.plot(x, y, color='b', linestyle=' ', marker='o', label='Data(x,y)')
              plt.plot(x, s4, color='r', linewidth=2, label='Data(x,f(x)=a+b/x')
              plt.legend(loc='best')
              plt.grid(True)
              plt.show()
x=[6.2, 6.5,7.4, 7.7, 8.2 ]

y=[2.618, 2.698,2.930, 3.004, 3.123]

mnkGP(x,y)
