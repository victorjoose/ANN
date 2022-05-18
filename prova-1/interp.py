import numpy as np

def poly(x,y):
    n = len(x)-1
    A =[]
    B =[]
    for xi in x:
        row = [1]
        for j in range(1, n+1):
            row.append(xi ** j)
        A.append(row)
    return np.linalg.solve(A, y)

def func_poly(x, coeffs):
    first = coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])

def f(x):
    return np.cos(np.exp(-x*x)) + np.sin((x*x)/2)

if __name__ == '__main__':

    # Exemplo 1
    x = [0.733, 1.762, 3.356]
    y = []

    # Para funções, deixar y vazio e usar:
    for i in x:
        y.append(f(i))

    coeffs = poly(x, y)
    print(coeffs)

    def p(x):
        return func_poly(x, coeffs)

    # visualização
    import matplotlib.pyplot as plt

    plt.scatter(x,y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]


    plt.plot(t, pt)
    plt.savefig('interp.png')
