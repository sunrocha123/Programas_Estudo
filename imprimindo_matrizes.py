def imprime_matriz(matriz):
    '''Esta função tem como objetivo, imprimir a matriz linha por linha'''

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == len(matriz[i]) - 1:
                print(matriz[i][j], end="")
            else:
                print(matriz[i][j], end=" ")
        print()

minha_matriz = [[1, 2], [3, 4]]
imprime_matriz(minha_matriz)
