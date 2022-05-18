import math

def troca_linhas(matrix, row1, row2):
    # row1 <-> row2
    new_row1 = []
    new_row2 = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row1:
                new_row2 = new_row2 + [matrix[i][j]]
            if i == row2:
                new_row1 = new_row1 + [matrix[i][j]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row1:
                matrix[i][j] = new_row1[j]
            if i == row2:
                matrix[i][j] = new_row2[j]


def combinacao_linear(matrix, row1, row2, a):
    # r1 + a*r2 -> r1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row1:
                matrix[i][j] = matrix[i][j] + a*matrix[row2][j]

    print_matrix(matrix)


def multiplica_linha(matrix, row, a):
    # a*row -> row
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row:
                matrix[i][j] *= a


def escalonamento(matrix):
    linha_pivo = 0

    for j in range(len(matrix[0])-2):
        for i in range(len(matrix)):
            if i > j:
                if not matrix[linha_pivo][j] == 0.0:
                    combinacao_linear(matrix, i, linha_pivo, -matrix[i][j]/matrix[linha_pivo][j])
                else:
                    error = 1
                    for k in range(i, len(matrix)):
                        if not matrix[k][j] == 0.0:
                            troca_linhas(matrix, k, linha_pivo)
                            combinacao_linear(matrix, i, linha_pivo, -matrix[i][j] / matrix[linha_pivo][j])
                            error = 0
                            break
                    if error == 1:
                        print("Error")
                        break

        linha_pivo += 1

    return matrix


def solucao(matrix):
    count = 1
    conjunto_solucao = []

    for i in range(len(matrix)-1, -1, -1):
        valor = matrix[i][len(matrix[0])-1]
        pos_solucao = 0
        for j in range(len(matrix[0])-2, len(matrix[0])-count-2, -1):
            if j == len(matrix[0])-count-1:
                valor /= matrix[i][j]
            else:
                valor -= matrix[i][j]*conjunto_solucao[len(conjunto_solucao)-1-pos_solucao]
                pos_solucao += 1

        conjunto_solucao = [round(valor, 16)] + conjunto_solucao
        count += 1

    return conjunto_solucao


def print_matrix(matrix):
    for i in range(len(matrix)):
        print('| ', end='')
        for j in range(len(matrix[0])):
            print('[' + str(matrix[i][j]) + '] ', end='')
        print('|')
    print()


if __name__ == '__main__':
    ang_a = 33 * math.pi / 180
    ang_b = 43 * math.pi / 180

    F4 = 1298
    F5 = 1017
    F6 = 764

    a1 = 21 * math.pi / 180
    a2 = 56 * math.pi / 180
    a3 = 79 * math.pi / 180

    # F4 = 2682
    # F5 = 0
    # F6 = 0

    # a1 = 90 * math.pi / 180
    # a2 = 90 * math.pi / 180
    # a3 = 90 * math.pi / 180

    F1h = -F4 * math.cos(a1)
    F2h = F5 * math.cos(a2)
    F3h = -F6 * math.cos(a3)

    F1v = -F4 * math.sin(a1)
    F2v = -F5 * math.sin(a2)
    F3v = -F6 * math.sin(a3)

    # [F1, F2, F3, H2, V2, V3, outro_valor]
    matrix = [
        [-math.cos(ang_a), 0, math.cos(ang_b), 0, 0, 0, -F1h],
        [-math.sin(ang_a), 0, -math.sin(ang_b), 0, 0, 0, -F1v],
        [math.cos(ang_a), 1, 0, 1, 0, 0, -F2h],
        [math.sin(ang_a), 0, 0, 0, 1, 0, -F2v],
        [0, -1, -math.cos(ang_b), 0, 0, 0, -F3h],
        [0, 0, math.sin(ang_b), 0, 0, 1, -F3v],
    ]

    print_matrix(matrix)

    matrix_escalonada = escalonamento(matrix)

    print(solucao(matrix_escalonada))