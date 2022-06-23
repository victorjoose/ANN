import random
import numpy as np
import math
def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def finite_diffs(x, order, x0, f):
    A = []
    B = []
    n = len(x)
    for i in range(n):
        A.append([0]*n)
        for j in range(n):
            A[i][j] = x[j] ** i
        potencias = [k + 1 for k in range(i - order, i)]
        fatorial = 0 if i < order else prod(potencias)
        termo = fatorial * x0 ** (i - order)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A,B)
    soma = 0
    for ck, xk in zip(cs, x):
        soma += ck * f(xk)
    return soma

def f(x):
    return  x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)

x0 = 0.0649
order = 5
x = [-0.1551, -0.1141, -0.0528, 0.0107, 0.0165, 0.0789, 0.1344, 0.1746, 0.2514, 0.2809]
values = [-0.1374, -0.0923, 0.0388, 0.1067, 0.199]

order1 = 1
order2 = 2
order3 = 3
order4 = 4
order5 = 5

p = 0
n = len(values)
for i in range(n):
    p = f(x0) + finite_diffs(x, order1, x0, f)*(values[i] - x0) + ((finite_diffs(x, order2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(x, order3, x0, f)/6) * ((values[i]-x0)**3)) + ((finite_diffs(x, order4, x0, f)/24) * ((values[i]-x0)**4)) + ((finite_diffs(x, order, x0, f)/120) * ((values[i]-x0)**5)) 
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{values[i]} = {p} e |f(x) - p3(x)| = {erroN}')

num_pontos = 0
a = x0 - 0.25
b = x0 + 0.25