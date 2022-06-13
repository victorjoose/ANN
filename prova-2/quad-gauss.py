import math


def p(x):
    return 1 - 3*x + 4* x**2 - 2 * x**3

r = math.sqrt(3)/3

aprox = p(-r) + p(r) + p

exato = 14/3

print (f'{aprox - exato = }')

def f(x):
        