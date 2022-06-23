import numpy as np

'''
Encontre os coeficientes a e b da função potência 
y=axb que melhor se aproxima da seguinte lista de 12 pontos
Dica: Tente escrever a equação y=axb na forma lny=lna+blnx. 

Isso se chama uma linearização da função não-linear original. 
Após isso, faça uma mudança de variáveis e use regressão linear 
para resolver o problema.
'''

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi**p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi*xi**i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*x**b


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':

    x = [0.5235, 0.7345, 1.0315, 1.1944, 1.37, 1.6441, 1.8371, 2.0136, 2.2064, 2.3786, 2.7796, 2.9092]
    y = [0.0854, 1.5327, 2.0592, 2.6658, 4.1657, 7.818, 12.0921, 15.7323, 21.6625, 27.7409, 46.515, 53.05]

    values = [0.7025, 1.423, 1.7937]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(yt)

    xt = [xi + k2 for xi in x]

    x_ = np.log(xt)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    print('Coeficientes da reta')
    print(f'{a0 = } e {a1 = }')

    print('Coeficientes da potencia')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(q(value))

    # visualização

    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    plt.savefig('best_poly_regressao_potencia.png')
