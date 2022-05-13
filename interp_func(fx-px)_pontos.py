import numpy as np
import math as npmath

def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])

def f(x):
   return np.exp(np.cos(x)**2)+np.exp(-x**2)+np.log(x)

# def f(x):
#     return 3.93506493 - 24.91831315*x + 22.47120031*x*x - 6.43426714*x*x*x + 0.5864879*x*x*x*x

# def f(x):
#     return 1/(1+25*x*x)

if __name__ == '__main__':
    x = [1.869, 2.808, 5.306, 6.167, 8.11]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)

    # print(f(2.084))
    # print(f(3.055))
    # print(f(3.554))

    # Econtrar Erros Absolutos
    print(abs(f(1.392) - p(1.392, coefs)))
    print(abs(f(2.105) - p(2.105, coefs)))
    print(abs(f(3.086) - p(3.086, coefs)))