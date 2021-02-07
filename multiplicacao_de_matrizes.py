def multiplicacao_de_matrizes(matriz1, matriz2):

    assert len(matriz1[0]) == len(matriz2)

    matriz_com_valores_multiplicados = []

    auxiliar_soma_multiplicacao = 0

    for i in range(len(matriz1)):
        lista = []
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                auxiliar_soma_multiplicacao += (matriz1[i][k] * matriz2[k][j])
            lista.append(auxiliar_soma_multiplicacao)
            auxiliar_soma_multiplicacao = 0
        
        matriz_com_valores_multiplicados.append(lista)

    return matriz_com_valores_multiplicados
        

if __name__ == "__main__":
    print(multiplicacao_de_matrizes([[2,3,1],[-1,0,2]],[[1,-2],[0,5],[4,1]]))
    print()
    print(multiplicacao_de_matrizes([[1,2],[3,4]],[[1,2,3],[3,5,4],[3,2,1]]))
