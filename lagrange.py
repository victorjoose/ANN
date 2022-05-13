
def lagrange(x, y):
    #retorna yi dividido pelo denominador do polinomio Li
    num = len(x)
    coefs = []
    for i in range(num):
        prod = 1
        for j in range(num):
            if i != j:
                prod *= (x[i] - x[j])
        ci = y[i] / prod
        coefs.append(ci)
    return coefs
    

def pl(t, x, coefs):
    soma = 0;
    num = len(coefs)
    for i in range(num):
        prod = 1
        for j in range(num):
            if i != j:
                prod *= (t - x[j])
        prod *= coefs[i]
        soma += prod
    return soma

def poly(x, coefs):
    def f(t):
        return pl(t, x, coefs)
    return f

if __name__ == '__main__':
    # ex
    x = [-1.781, -0.187, 0.9, 1.613, 3.122, 4.015, 5.517, 6.51]  # coordenadas x do ponto
    y = [0.588, 0.978, 0.914, 0.678, -0.434, -0.948, -0.469, 0.447]  # coordenadas y do ponto

    # x = [-0.836, 0.156, 0.858] 
    # y = [0.054, 0.622, 0.052]

    coefs = lagrange(x, y)
    print(coefs)

    lagr = poly(x, coefs)
    print(lagr(0), lagr(1), lagr(2))
    # print(lagr(2.5))


    #visualização
    import matplotlib.pyplot as plt
    import numpy as np

    plt.scatter(x, y)

    t = np.linspace(min(x), max(y), 100)
    lt = [lagr(ti) for ti in t]
    plt.plot(t, lt)
    plt.savefig('lagrange.png')