import numpy as np
import best_poly as bp

def poly(x, a, b):
    return a * np.exp(b * x)


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x = [0.0083, 0.2563, 0.3975, 0.5879, 0.6972, 0.9262, 1.0205, 1.2174, 1.4442, 1.5246, 1.7716, 1.9926]
    y = [5.0737, 6.6263, 8.5914, 10.779, 11.113, 22.7253, 22.051, 33.3366, 43.8111, 52.26, 70.172, 100.69]
    y_ = np.log(y)

    grau = 1

    a0, a1 = bp.best_poly_func_exp(x, y_, grau)

    a = np.exp(a0)
    b = a1

    print(f'{a = } e {b = }')

    p = build_func(a, b)
    
    x_values = [0.9222, 1.0378, 1.6648]
    
    for xi_v in x_values:
        print(p(xi_v))
