#include <stdio.h>
#include <math.h>

#define ROW 3
#define COL 3

void imprimeMatriz(double matriz[ROW][COL]){
    for(int row = 0; row < ROW; row++){
        for(int col = 0; col < COL; col++){
            printf("%.16f ", matriz[row][col]);
        }
        printf("\n");
    }
}

void trocaLinha(double matriz[ROW][COL], int r1, int r2){
        for(int k=0;k<COL;k++){
        double temp = matriz[r1][k];
        matriz[r1][k] = matriz[r2][k];
        matriz[r2][k] = temp;
    }
}

void operacaoEmLinha(double matriz[ROW][COL], double num, int row){
    for(int i = 0; i < COL; i++){
        matriz[row][i] *= num; 
    }
}

void operacaoEmDuasLinhas(double matriz[ROW][COL], double num, int r2,  int target){
    for(int i = 0; i < COL; i++){
        matriz[target][i] = (num*matriz[r2][i]) + matriz[target][i];
    }
}

void operacoes(double matriz[ROW][COL]){

    operacaoEmLinha(matriz, (4.0/3.0), 2);
    trocaLinha(matriz, 0, 1);
    operacaoEmDuasLinhas(matriz, (9.0/4.0), 1, 2);

    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
        {2.0/1.0, 9.0/2.0, 1.0/2.0},
        {-2.0/3.0, 2.0/3.0, 3.0/4.0},
        {-8.0/3.0, -8.0/9.0, -3.0/7.0}
    };

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("Resultado:\n");
    operacoes(matriz);
    return 0;
}