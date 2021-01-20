import numpy as np
#from random import randint
#l = [randint(10,80) for x in range(10)]


def inverse(C):
    E = 0.01
    length = len(C)
    det = np.linalg.det(C)
    print(det)
    matrixx = [[0 for x in range(length)] for y in range(length)]
    inv_mas = [[0 for x in range(length)] for y in range(length)]
    mas1 = [[0 for x in range(length)] for y in range(length)]
    for i in range(length):  # список C копіюємо в другий список
        for j in range(length):
                matrixx[i][j] = C[i][j]
    for u in range(length):
      m = [[0 for x in range(length)] for y in range(length)]#створюємо додаткові списки
      b = [[0 for x in range(length)] for y in range(length)]
      x = [0 for x in range(length)]

      for i in range(length):  # список C копіюємо в другий список
        for j in range(length):
            if i == j:
                b[i][j] = 1
                mas1[i][j]=1
      for i in range(length):  # список C копіюємо в другий список
          for j in range(length):
                C[i][j]=matrixx[i][j]
      l = 0
      for k in range(length):

        ss = C[k][k]
        g=k
        for j in range(k+1,length):
            mm=C[j][k]
            if abs(mm) > abs(ss):
               g = j
               ss=mm


        if abs(ss) < 0.01:
           print("Розв'язку немає")
        if g!=k:
            l = l + 1
        for j in range(k, length):

            ss=C[k][j]
            C[k][j]=C[g][j]
            C[g][j]=ss

        hh = b[k][u]
        b[k][u] = b[g][u]
        b[g][u] = hh

        for i in range(k+1, length):
            m[i][k]=-C[i][k] / C[k][k]
            #for q in range(length):
            b[i][u]=b[i][u]+m[i][k] * b[k][u]
            for j in range(k + 1, length):
                C[i][j]=C[i][j]+m[i][k] * C[k][j]


      det=1.0;
      for i in range (length):
        det*=C[i][i]
      if(u==length-1):
          f = open('tex.txt', 'a')
          if(l%2==1):
              f.write("Визначник: " + str(-det))
              f.write('\n')
          else:
              f.write("Визначник: " + str(det))
              f.write('\n')

      x[length-1] = b[length-1][u]/C[length-1][length-1]
      for k in range(length-1,-1,-1):

        p=0
        for j in range(k+1,length):
            p +=C[k][j]*x[j]
        x[k]=(b[k][u]-p)/C[k][k]
      for i in range(length):
        inv_mas[i][u] = x[i]
    print(inv_mas)
    f = open('tex.txt', 'a')
    for i in range(length):
        for j in range(length):
            f.write(str(inv_mas[i][j]) + ' ')
        f.write('\n')
    O = np.zeros((length, length))  # Перевірка(множимо матрицю на її обернену матрицю):
    for i in range(length):
        for j in range(length):
            for k in range(length):
                O[i][k] += matrixx[i][j] * inv_mas[j][k]
    print(O)

    f.write("Одинична матриця: ")
    f.write('\n')
    for i in range(length):
        for j in range(length):
            f.write(str(O[i][j]) + ' ')
        f.write('\n')
    var_a = 0.0
    a, b = 0, 0
    for i in range(length):
        for j in range(length):
            if 0.5 > abs(O[i][j]) > var_a:  # шукаємо найбільшу похибку(абсолютна)
                var_a = abs(O[i][j])
                a = i
                b = j

    #f.write("Абсолютна похибка: " + str(var_a))
    #f.write('\n')
    #f.write("Відносна похибка: " + str(abs(var_a / inv_mas[a][b])))
    #f.write('\n')

    O1 = np.zeros((length, length))
    for i in range(length):
        for j in range(length):
            O1[i][j]=O[i][j]-mas1[i][j]

    Z = 0
    for i in range(length):
        for j in range(length):
            Z+=(O1[i][j])**2
    f.write("Похибка: " + str(Z**0.5))
    f.write('\n')
    f.write('\n')
    f.close()
    return inv_mas

handle = open("matrix.txt", "r")#відкриваємо файл
data = handle.readlines()#зчитуємо
#print(data)
word_list = []
for i in range(len(data)):
       word_list.append(data[i].split())
#запис матриць в змінні
A = [[int(j) for j in word_list[i]] for i in range(4)]
B = [[int(j) for j in word_list[i+5]] for i in range(3)]
C = [[int(j) for j in word_list[i+9]] for i in range(4)]
handle.close()
k = np.random.random ([100,100]) * 10

inverse(inverse(A))
inverse(B)
inverse(C)
inverse(k)
