#include <stdio.h>
#include <math.h>

#include "functions.h"

void newton (double (*f)(double),double (*df)(double),double x0, int n) {
    for (int i = 0; i < n; i++){
        double dfx0 = df(x0);
        if (dfx0 == 0) {
            printf("Divisão por zero, não foi possível executar a iteração %d do método de Newton.", i+1);
            return;
        } else {
            x0 = x0 - f(x0) / dfx0;
            printf("x_%d = %.16f\n", i + 1, x0);
        }
    }
}

double f (double x) {
    return exp(5*x) - 2;
}

double df(double x) {
    return 5 * exp(5*x);
}

int main() {
    double x0 = 22.78;
    int n = 5;

    // newton(populational_growth, d_populational_growth, x0, n);
    newton(sky_diver_velocity, d_sky_diver_velocity, x0, n);
}