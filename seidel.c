#include <stdio.h>

void seidel(double *x0, int rows, double matrix[rows][rows+1], int n){
    for(int i=0; i<n; i++){
        for(int r =0; r<rows; r++){
            double temp = 0;
            temp += matrix[r][rows];
            for(int c = 0; c<rows; c++){
                if(r!=c){
                    temp -= (matrix[r][c] * x0[c]);
                }
            }
            temp /= matrix[r][r];
            printf("X_%d,%d = %.16f\n", r + 1, i + 1, temp);
            x0[r] = temp;
        }
        printf("\n");
    }
}

int main(){
    
    // int rows = 3;
    // double matrix[3][4] = {
    //     {-4.31, -0.72, -2.37, -3.43},
    //     {3.08, 4.38, 0.08, 3.17},
    //     {-3.75, 4.37, -9.34, -3.35}
    // };
    // double x0[3] = {-3.59, 3.7, -4.52};


    int rows = 4;
    double matrix[4][5] = {
        {-7.58, 2.25, 2.18, 1.59, -1.83},
        {-1.87, -8.48,-0.09, 4.96, -0.93},
        {-3.13, -0.55, -10.09, -4.86, 3.01},
        {2.85, 2.01, -0.78, -7.2, 1.75}
    };
    double x0[4] = {-3.12, 1.5, 3.96, -3.03};

    int n = 18;

    seidel(x0, rows, matrix, n);
}