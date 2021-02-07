def dimensoes(matriz):
    '''Esta função tem como objetivo, exibir ao usuário
    o número de linhas e colunas que possui a matriz digitada'''

    lin = len(matriz) # nº total de linhas
    col = len(matriz[0]) # nº total de colunas
    print(str(lin) + "X" + str(col))


minha_matriz = [[1,2],[3,4],[3,9]]

dimensoes(minha_matriz)