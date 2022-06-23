import math
import numpy as np


def richardson(col_1):
    n = len(col_1) - 1
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]


if __name__ == '__main__':
    approximations = [-0.3722522758161446, -0.7451037635915156, -0.9296974353193264, -1.0212200701648726, -1.066749249734471, -1.089451061535101]

    new_value = richardson(approximations.copy())
    aprox = richardson(approximations + [new_value])
    print(aprox)
