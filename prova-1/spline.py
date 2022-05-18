import numpy as np
import matplotlib.pylab as plt

def spline(x, y):
    n = len(x)
    a = {k: v for k, v in enumerate(y)}
    h = {k: x[k + 1] - x[k] for k in range(n - 1)}

    A = [[1] + [0] * (n - 1)]
    for i in range(1, n - 1):
        row = [0] * n
        row[i - 1] = h[i - 1]
        row[i] = 2 * (h[i - 1] + h[i])
        row[i + 1] = h[i]
        A.append(row)
    A.append([0] * (n - 1) + [1])

    B = [0]
    for k in range(1, n - 1):
        row = 3 * (a[k + 1] - a[k]) / h[k] - 3 * (a[k] - a[k - 1]) / h[k - 1]
        B.append(row)
    B.append(0)

    c = dict(zip(range(n), np.linalg.solve(A, B)))

    b = {}
    d = {}
    for k in range(n - 1):
        b[k] = (1 / h[k]) * (a[k + 1] - a[k]) - (h[k] / 3) * (2 * c[k] + c[k + 1])
        d[k] = (c[k + 1] - c[k]) / (3 * h[k])

    s = {}
    for k in range(n - 1):
        print(f'Equation {k}:')
        print(f'a[{k}] = {a[k]}')
        print(f'b[{k}] = {b[k]}')
        print(f'c[{k}] = {c[k]}')
        print(f'd[{k}] = {d[k]}')
        eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
        s[k] = {'eq': eq, 'domain': [x[k], x[k + 1]]}

    return s

# x = []
# y = []
# z = [(0.493,5.351), (1.155,5.348), (1.741,5.361), (2.148,4.998), (2.75,4.742), (3.539,4.067), (4.029,3.066), (4.722,2.986)]
# # z = [(0.499,1.835) , (0.803,1.665), (1.629,2.803), (1.908,2.913), (2.43,1.612), (3.185,0.673), (3.912,2.705)]

# for xi, yi in z:
#     x.append(xi)
#     y.append(yi)

# usando com função
x = [0.319, 1.298, 2.218, 2.745]
y = []

def f(x):
    return np.cos(np.sin(np.log(x*x)))
    # return np.sin(np.sqrt(np.pi+(x*x)))

for xi in x:
    y.append(f(xi))

eqs = spline(x, y)

for eq in eqs.values():
    print(eq)


def s(x):
    for key, value in eqs.items():
        if value['domain'][0] <= x <= value['domain'][1]:
            return eval(value['eq'])

# print(s(3.124))
# print(s(3.154))
# print(s(4.647))           


# visu
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f'$S_{key}(x)$')

plt.scatter(x, y)
plt.legend()
plt.savefig('spline.png')