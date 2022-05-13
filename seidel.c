#include <stdio.h>
#include <math.h>
#define ROWS 3
#define COLS 3

void seidel(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n){
    for(int it = 0; it < n; it++){
        for(int i=0; i<ROWS; i++){
            double xi = b[i];
            for(int j = 0; j<COLS; j++){
                if(i!=j){
                    xi -= a[i][j] * chute[j];
                }
            }
            xi /= a[i][i];
            chute[i] = xi;
        }
        printf("X^(%d) ->", it +1);
        for(int k=0;k<COLS; k++){
            printf("%.8f\t", chute[k]);
        }
        printf("\n");

    }
}

int main() {
    double g = 9.81, k = 52 * M_PI/180,
            mi1 = 0.19, mi2 = 0.19, mi3 = 0.5,
            m1 = 139, m2 = 123, m3 = 23,
            r1 = (m1 * g * sin(k)) - (mi1 * m1 * g * cos(k)),
            r2 = (m2 * g * sin(k)) - (mi2 * m2 * g * cos(k)),
            r3 = (m3 * g * sin(k)) - (mi3 * m3 * g * cos(k));

    printf("%.16f,   %.16f,   %.16f", r1, r2, r3);

    // Seidel input
    double a[ROWS][COLS] = {
        {m1, 1, 0},
        {m2, -1, 1},
        {m3, 0, -1}
    };

    double b[ROWS] = {r1, r2, r3};

    double chute[COLS] = {5, 148, 127};

    int n = 300;

    seidel(a,b,chute,n);

    return 0;
}
