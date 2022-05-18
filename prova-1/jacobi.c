#include<stdio.h>

#define ROWS 3
#define COLS 3

void jacobi(double a[ROWS][COLS], double b[COLS], double x0[COLS], int n){
    for(int it = 0; it < n; it++){
        double temp[COLS];
        for(int i =0; i < ROWS; i++){
            double xi = b[i];
            for(int j=0; j<COLS; j++){
                if(i != j){
                    xi -= a[i][j] * x0[j];
                }
            }
            xi /= a[i][i];
            temp[i] = xi;
        }
        printf("X^(%d) -> ", it + 1);
        for(int k=0; k < COLS; k++){
            x0[k] = temp[k];
            printf("%.10f\t", x0[k]);
        }
        printf("\n");
    }
}
int main(){
    // 3x3
    double a[ROWS][COLS] = {{-6.5, -0.49, -4.27}, {2.91, 8.22, 3.57}, {-3.73, -2.97, -8.45}};
    double b[ROWS] = {2.61, 1.09, -2.35};
    double x0[COLS] = {1.39, 2.69, 4.02};

    //4x4
    // double a[ROWS][COLS] = {{-10.05, -1.69, 2.06, -4.6}, {-1.03, 6.73, 3.43, -0.55}, {1.44, -0.17, 7.62, 4.3}, {0.74, -4.86, 0.66, 7.98}};
    // double b[ROWS] = {2.84, -4.52, 1.8, -2.6};
    // double x0[COLS] = {-4.27, -4.65, 3.57, -4.51};

    int n = 18;

    jacobi(a, b, x0, n);
}