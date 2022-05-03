#include <stdio.h>
#include <math.h>

void secante(double (*f)(double), double x0, double x1, int n){
    for(int i = 0; i < n; i++){
        double result = f(x1) - f(x0);
        if(result == 0){
            printf("Divisão por zero na iteração %d\n", i+1);
            return;
        }
        double x2 = (x0 * f(x1) - x1 * f(x0)) / result;
        printf("x_%d = %.16lf\n", i+1, x2);
        x0 = x1;
        x1 = x2;
    }
}

double f(double x){
    return x - 1 - 3 * sin(x);
}

int main(){
    double x0 = 1.4874;
    double x1 = 2.53815;
    int n = 5;

    secante(f, x0, x1, n);
}