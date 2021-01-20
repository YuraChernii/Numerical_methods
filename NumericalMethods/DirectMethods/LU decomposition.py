import numpy as np

a = np.array([[0.34, -7.9, 0.3],
              [11.3, 2.8, -1.3],
              [1.8, 2.4, 7.7]])

b = np.array([-4.1, 0.7, 0.48])
res = float(0)
def check_result(a,b,c):
    for i in range(len(b)):
        res = 0
        for j in range(len(b)):
            res+=float(a[i][j]*c[j])
        if abs(res - b[i]) > 0.000001:
            return False
    return True


def return_LU(a):
    LU = np.matrix(np.zeros([a.shape[0], a.shape[1]]))
    n = a.shape[0]
    for k in range(n):
        for j in range(k, n):
            LU[k, j] = a[k, j] - LU[k, :k] * LU[:k, j]
        for i in range(k + 1, n):
            LU[i, k] = (a[i, k] - LU[i, : k] * LU[: k, k]) / LU[k, k]
    return LU


def return_solve(LU, b):
    y = np.matrix(np.zeros([LU.shape[0], 1]))
    x = np.matrix(np.zeros([LU.shape[0], 1]))
    for i in range(y.shape[0]):
        y[i, 0] = b[i] - LU[i, :i] * y[:i]
    for i in range(1, x.shape[0] + 1):
        x[-i, 0] = (y[-i] - LU[-i, -i:] * x[-i:, 0]) / LU[-i, -i]
    return x


print(a)
LU = return_LU(a)
c = return_solve(LU, b)
for i in range(len(b)):
    print("x"+str(i+1)+" = "+str(c[i]))
print("check result: ", end='')
print(check_result(a, b, c))



#[[ 0.34 -7.9   0.3 ]
# [11.3   2.8  -1.3 ]
# [ 1.8   2.4   7.7 ]]
#x1 = -0.07432109
#x2 = 0.51274672
#x3 = -0.08010574
#check result: True
