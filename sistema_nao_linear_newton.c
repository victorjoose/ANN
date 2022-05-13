#include <stdio.h>
#include <math.h>
#define ROWS 6 // CONFERIR 
#define COLS 7 // CONFERIR

// X0 E Y0, chute INSERIR LA EM BAIXO

double g1(double x, double y){  //func 1
    return x*x + y*y - 5;
}

double g2(double x, double y){ //func 2
    return x*x + x*y*y*y - 3;
}

double g1x(double x, double y){ // derivada func 1 em X
    return 2*x;
}

double g1y(double x, double y){ // derivada func 1 em y
    return 2*y;
 }

double g2x(double x, double y){ // derivada func 2 em x
    return 2*x + y*y*y;
}
double g2y(double x, double y){ // derivada func 2 em y
    return 3*x*y*y;
}

double det(double x, double y){
     return g1x(x,y)*g2y(x,y)-g1y(x,y)*g2x(x,y);
}

void newton(double x, double y, int n){
    for(int k=0;k<n;k++){
        double d=det(x,y);
        if(d==0){
            printf("nao eh possivel continuar\n");
            return;
        }  
        double xk=x-(g2y(x,y)*g1(x,y)- g1y(x,y)*g2(x,y))/d;
        double yk=y-(-g2x(x,y)*g1(x,y)+ g1x(x,y)*g2(x,y))/d;
        printf("x^(%d) = %.16f\n", k+1, xk);
        printf("y^(%d) = %.16f\n\n", k+1, yk);
        x=xk;
        y=yk;
    }
}
    
int main(){
    double x0= -0.6423;
    double y0= -1.9941;
    int n=5;
    newton(x0,y0,n);
     
    return 0;
}