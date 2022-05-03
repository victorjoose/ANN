#include <stdio.h>
#include <math.h>

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

int main() {
//Example 1: f(xe) = x³ - 2, (0,2)
double f(double x) {
    return x * x - 5.0;
}

double a = -2.80016;
double b = -1.51458;
int n = 12;

// Função:
double P(double x){
    double e = exp(x);
    return e - 2 * x * x + x - 1.5;
}


// Valores:
double a1 = 0.09264; 
double b1 = 0.75199;
int n1 = 12;


// bisection(f, a, b, n);
bisection(P, a1, b1, n1);
}