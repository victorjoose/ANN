#include <stdio.h>
#include <math.h>

#include "functions.h"

void bisection(double (*f)(double), double a, double b, int n) {
    if (f(a) * f(b) >= 0) {
        printf("Não é possível usar Bolzano para garantir a existencia de uma raiz em [%f, %f]\n", a, b);
    } else {
        for (int i = 0; i < n; i++) {   
            double m = 0.5 * (a + b);
            printf("x_%d = %.16f\n", i + 1, m);
            if (f(m) == 0) {
                printf("Você encontrou uma raiz r = %.16f", m);
                return;
            }
            if (f(a) * f(m) < 0) {
                b = m;
            } else {
                a = m;
            }
        }
    }
}

//Example 1: f(xe) = x³ - 2, (0,2)
    double f(double x) {
        return x * x - 5.0;
    }


int main() {
    
    double a = 22.0;
    double b = 194.91;
    int n = 12;

    bisection(sky_diver_velocity, a, b, n);
}