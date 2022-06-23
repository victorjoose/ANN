import numpy as np
import math

'''
a * (x/(x+b))
Encontre os coeficientes a e b da função taxa de crescimento da 
saturação y= a*(x/(x+b)) que melhor se aproxima da 
seguinte lista de 12 pontos
'''

def best_line(x, y, grau=1):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * (x/(x+b))

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x = [2.3961, 3.8956, 4.4498, 6.1861, 8.6882, 9.8611, 11.1253, 13.0851, 14.3335, 15.6937, 17.7293, 19.3412]
    y = [2.1012, 2.6175, 2.745, 3.0377, 3.3392, 3.4965, 3.5154, 3.6021, 3.6678, 3.6971, 3.7897, 3.7853]

    values = [11.4166, 15.8601, 18.3085]

    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = (np.divide(1,y))

    xt = [xi + k2 for xi in x]

    x_ = np.divide(1,x)
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = 1/a0

    b = a1/a0
    print('Coeficientes da reta')
    print(f'{a0 = } e {a1 = }')

    print('Coeficientes')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px = }')

    # visualização

    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    plt.savefig('best_poly_regressao_potencia.png')
