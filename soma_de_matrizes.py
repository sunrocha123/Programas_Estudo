def soma_matrizes(matriz1,matriz2):
    '''Esta função recebe duas matrizes e valida se suas dimensões são iguais.
    Caso seja, é realizada a soma dos elementos. Caso contrário, será devolvido a palavra False'''

    if len(matriz1) != len(matriz2):
        return False
        pass
    else:
        nova_matriz = [] # está matriz receberá a soma dos elementos
        for i in range (len(matriz1)):
            lista = [] # lista vazia
            for j in range(len(matriz1[0])):
                if len(matriz1[i]) != len(matriz2[i]):
                    return False
                    pass
                lista.append(matriz1[i][j] + matriz2[i][j])
            nova_matriz.append(lista)
        return nova_matriz
        pass




def test_answer():
    m1 = [[3,4,5],[4,4,12]]
    m2 = [[3,5,6],[6,7,8],[9,10,11]]
    m3 = [[1,2,3],[3,4,5],[12,33,44]]
    m4 = [[1,44,55],[66,101,150],[122,113,114]]
    m5 = [[1,2,4],[1,2]]
    m6 = [[1,1],[5,6]]
    assert soma_matrizes(m1, m2) == False
    assert soma_matrizes(m3, m4) != False
    assert soma_matrizes(m5, m6) == False
