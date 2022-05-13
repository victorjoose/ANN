#include <stdio.h>
#include <math.h>

#define ROW 4
#define COL 4

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

void operacaoEmLinha(double matriz[ROW][COL], int row, double num){
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

    operacaoEmDuasLinhas(matriz, (-1.0/2.0), 0, 1);
    operacaoEmDuasLinhas(matriz, (1.0/4.0), 0, 2);
    operacaoEmDuasLinhas(matriz, (3.0/2.0), 0, 3);
    operacaoEmDuasLinhas(matriz, (-7.0/12.0), 1, 2);
    operacaoEmDuasLinhas(matriz, (-36.0/13.0), 2, 3);
    

    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
        {-4.0/1.0, -2.0/1.0, 5.0/1.0, 2.0/1.0},
        {-2.0/1.0, 5.0/1.0, -2.0/1.0, -1.0/1.0},
        {1.0/1.0, 4.0/1.0, 1.0/1.0, 1.0/1.0},
        {6.0/1.0, 3.0/1.0, 6.0/1.0, -3.0/1.0}
    };

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("Resultado:\n");
    operacoes(matriz);
    return 0;
}