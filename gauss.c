/*
Método de elimação do gauss (escalonamento)

// Def: Seja  uma matriz m x n. A diagonal do A é a lista de elementos aij onde i=j

A =  {[2, 1, 3],
      [4, 1, 2]}

Estar abaixo da diagonal significa que o número de linhas é sempre menor que o de colunas (i > j)

*/
#include <stdio.h>

#define ROWS 3
#define COLS 2

void print_matrix(double matrix[ROWS][COLS]) {
    for (int i = 0;i < ROWS; i++) {
        for(int j = 0; j < COLS; j++) {
            printf("%.8f\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void gauss(double E[ROWS][COLS]) {
    for (int j = 0; j < COLS ; j++) {
        for (int i = j; j < ROWS; i++) {
            if (E[i][j]!= 0) {
                if(i != j) { 
                    // trocar linhas
                    for (int k = 0; k < COLS - 2; k++) {
                        double aux = E[i][k];
                        E[j][k] = E[j][k];
                        E[j][k] = aux;
                    }
                }
                // aplicar operações elementares em linha
                // a * Lj + Lm -> Lm
                for (int m = j + 1; m < ROWS; m++) {
                    double a = -E[m][j]/E[j][j];
                    for (int n = j; n < COLS; n++) {
                        E[m][n] += a * E[j][n];
                    }
                }
                print_matrix(E);
                printf("\n");
                break; //para de procurar elementos diferentes de 0
            }
            else {
                if(i == ROWS - 1){
                    printf("Sistema não tem solução");
                }
            }
        } 
    } 
}

void reverse_sub(double E[ROWS][COLS]) {
    int last = ROWS - 1;
}

int main() {
    double E[ROWS][COLS] = {
        {-1, 1},
        {4/3, -1/3},
        {-3/5, 1}
    };
    
    // double E[ROWS][COLS] = {
    //     {2,4,6,2,4},
    //     {1,2,-1,3,8},
    //     {-3,1,-2,1,-2},
    //     {1,3,-3,-2,6}
    // };

    print_matrix(E);

    gauss(E);

    // reverse_sub(E);
}