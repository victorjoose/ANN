#include <stdio.h>
#include <math.h>
#define L 3
#define C 3

void jacobi(double A[L][C], double B[L], double chute[L], int n){
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("x_%d(%d) = %.16f | ", i+1, k+1, bi);
            chute[i]=bi;
        }
        printf("\n");
    }
}


// INSERIR O TAMANHO DA MATRIZ EM DEFINE
//***************************************************************************

int main(){
    double A[L][C]={{-6.5, -0.49, -4.27},{2.91, 8.22, 3.57},{-3.73, -2.97, 3.57}};
    double B[L]={2.61, 1.09, -2.35}; // result

    double chute[L]= {1.39,2.69,4.02}; //x0
    int n=20;

    jacobi(A, B, chute, n);

    return 0;
}