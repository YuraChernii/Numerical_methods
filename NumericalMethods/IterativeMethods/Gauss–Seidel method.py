import numpy as np


a = np.array([
    [11.3, 2.8, -1.3],
    [0.34, -7.9, 0.3],
    [1.8, 2.4, 7.7]])

b = np.array([0.7,-4.1, 0.48])


def G_S(a, b, x, g):
    x = x.astype(float)
    m, n = a.shape
    times = 0
    while True:
            for i in range(n):
                s1 = 0
                tempx = x.copy()
                for j in range(n):
                    if i != j:
                        s1 += x[j] * a[i][j]
                x[i] = (b[i] - s1) / a[i][i]
                times += 1
            gap = max(abs(x - tempx))

            if gap < g:
                break

            elif times > 1000000:
                print("Think about it))")
                break
    print("Eps = " + str(g))
    print("Steps: "+str(times))
    for i in range(len(b)):
        print("x" + str(i + 1) + " = " + str(x[i]))


if __name__ == '__main__':
    x = np.array([-0.5, 1, 0.5])
    g = 1e-10
    G_S(a, b, x, g)


#Eps = 1e-10
#Steps: 30
#x1 = -0.07432108691859053
#x2 = 0.5127467226865396
#x3 = -0.08010573740184834
