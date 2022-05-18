import numpy as np

def lagrange(x, y):
    for i in range(len(x)):
        a = 1
        for j in range(len(x)):
            if i != j:
                a *= (x[i]-x[j])
        print(y[i]/a)


if __name__ == '__main__':
    # x = [-1.781, -0.187, 0.9, 1.613, 3.122, 4.015, 5.517, 6.51]  # coordenadas x do ponto
    # y = [0.588, 0.978, 0.914, 0.678, -0.434, -0.948, -0.469, 0.447]  # coordenadas y do ponto

    # x = [-0.535, 0.235, 0.709]
    # y = [0.123, 0.42, 0.074]

    x = []
    y = []
    z = [0.347, 0.644, 1.335, 1.552, 2.095, 2.299, 2.652]

    def f(x):
        return np.cos(np.sin(np.log(x**2)))
        # return 1/(1+25*x*x)

    for i in z:
        x.append(i)
        y.append(f(i))

    lagrange(x, y)