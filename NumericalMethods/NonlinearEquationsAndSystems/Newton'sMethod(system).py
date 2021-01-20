import numpy as np
from sympy import *
import math


def jacobian(xy):
    x, y = xy
    return [[2*x*(y**2) - 6*x, 2*y*(x**2)- 18*y**2],
            [4*x**3, -9]]


def func(xy):
    x, y = xy
    return [(x**2)*(y**2)-3*(x**2)- 6*(y)**3 + 8, (x**4)-9*y+2]


def check_result(xy):
    x, y = xy
    if (x**2)*(y**2)-3*(x**2)- 6*(y)**3 + 8<00000.1 and (x**4)-9*y+2 < 00000.1:
        return True


def iter_newton(fun, x_init, jacobian, epsilon):
    max_iter = 100000

    times = 0
    x_last = x_init

    for k in range(max_iter):
        #J(xn)*( xn+1 - xn ) = -F(xn):
        J = np.array(jacobian(x_last))

        F = np.array(fun(x_last))

        diff = np.linalg.solve(J, -F)

        x_last = x_last + diff


        if np.linalg.norm(diff) < epsilon:

            times = k
            break
    else:
        print('nea')
    print('Starting points:',x_init)
    print("Eps = " + str(epsilon))
    print('Result:', x_last)

    print("Steps: " + str(times))
    return x_last


x_sol = iter_newton(func, [1.0,2.0], jacobian, 1e-8)
print('Check result:',check_result(x_sol))


