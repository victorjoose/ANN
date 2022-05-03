#include <stdio.h>
#include <math.h>

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
    return x * x - 4 * x + 2 - log(x);
}

double df(double x) {
    return 2 * x - 4 - 1/x;
}

int main() {
    double x0 = 1.21452;
    int n = 5;

    newton(f, df, x0, n);
}