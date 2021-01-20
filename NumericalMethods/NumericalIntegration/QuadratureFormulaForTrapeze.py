import math


def f(xk):
 y = (xk**(1/2) * math.cos(0.35*xk))/(0.35+xk)**2
 return y


if __name__ == "__main__":
 A = float(0)
 B = float(0.6)
 eps = 0.5e-6
 S = 0

 Sold = float(0)
 Sn = float(0)
 k = 1
 N = int(input("Enter N:"))
 k = 1
 var1=1
 while abs(S - Sold) > eps or int(var1)==int(1):
  var1=0
  Sold = S
  H = (B - A)/N
  S = 0
  S = (f(A) + f(B))/2
  x = A + H
  for i in range(N):
     S = S + f(x)
     x = x + H
  S = S * H
  print("S = ", end='')
  print(S)
  print(" eps = ", end='')
  print(abs(S - Sold))
  print("N = ",end='')
  print(N)
  N = N * 2

