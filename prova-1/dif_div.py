import numpy as np

def dif_div(x, y):
    num = len(x)
    Y = [yi for yi in y]
    coefs = [y[0]]
    for j in range(num -1):
        for i in range(num - 1 - j):
            numerador = Y[i + 1] - Y[i]
            denominador = x[i + 1 + j] - x[i]
            div = numerador / denominador
            Y[i] = div
        coefs.append(Y[0])
    return coefs

def poly(t, x, coefs):
    val = 0
    num = len(coefs)
    for i in range(num):
        prod = 1
        for j in range(i):
            prod *= (t - x[j])
        val += coefs[i] * prod
    return val

def build_func(x, coefs):
    def temp(t):
        return poly(t, x, coefs)
    return temp


if __name__ == '__main__':

    #ex
    # x = [-2.778, -1.221, -0.665, 0.792, 2.182, 2.962, 4.285]
    # y = [1.931, 1.275, 2.726, 2.333, 1.47, 1.984, 1.272]

    # coefs = dif_div(x, y)

    # #polinomio interpolador da lista de pontos
    # p = build_func(x, coefs)

    # print(coefs)

    # print(p(1), p(3), p(3), p(4))
    # print(f'{p(0.97244)}')


    # Usando Função
    # x = [0.537, 1.492 , 2.77]
    x = [0.988, 1.937, 2.867]
    y = []

    def f(x):
        return np.cos(np.sin(np.log(x**2)))
        # return pow(np.cos(x),3)+2*pow(np.cos(x),2)+1 

    for i in x:
        y.append(f(i))

    coefs = dif_div(x, y)
    p = build_func(x, coefs)
    print(coefs)



    #visu
    import matplotlib.pyplot as plt

    t = np.linspace(min(x), max(x), 100)
    pt = [p(ti) for ti in t]

    plt.scatter(x, y)
    plt.plot(t, pt)

    plt.savefig('dif_div.png')