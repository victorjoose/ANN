#include <stdio.h>
#include <math.h>

#include "functions.h"

void fpos(double (*f)(double), double a, double b, int n){
    double fa = f(a);
    double fb = f(b);

    if(fa * fb >= 0){
        printf("Nao sei dizer se f possui raiz no intervalo [%f,%f]\n", a, b);
        return;
    } else{
        for(int i = 0; i < n; i++){
            double x = (a * fb - b * fa)/(fb-fa);
            printf("x_%d = %.16f\n", i + 1, x);
            double fx = f(x);
            if(fx == 0){
                printf("a raiz procurada é: x = %.16f\n", x);
                return;
            }
            if(fa * fx < 0){
                b = x;
                fb = fx;
            } else {
                a = x;
                fa = fx;
            }
        }
    }
}

 
double f(double x){
    // return PI * x - exp(x);
    return exp(5*x) - 2;
}

int main(){
    double a = 30.05;
    double b = 187.44;
    int n = 11;

    // fpos(f, a, b, n);
    fpos(sky_diver_velocity, a, b, n);
    return 0;
}