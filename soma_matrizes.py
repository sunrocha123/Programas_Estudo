def gerar_matriz():
    ''' Está função tem como objetivo gerar os valores da matriz'''

    matriz = [] # matriz que receberá os valores processados

    for i in range(5):
        lista = [] # lista vazia
        for j in range(5):
            lista.append(j + i + 1) # comando para adicionar os valores processados na lista
        matriz.append(lista) # comando para adicionar na matriz os valores da lista

    for k in range (len(matriz)): # comando para exibir a matriz processada
        for q in range(len(matriz[k])):
            print(matriz[k][q], end=" ")
        print()
    
    soma_impar(matriz)

def soma_impar(matriz):
    ''' Está função tem como objetivo somar todos os valores ímpares da matriz'''

    tot_impar = 0 # Está variável irá receber a soma de todos os valores ímpares da matriz

    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 != 0:
                tot_impar += matriz[i][j]
    
    print('\nA soma dos valores ímpares da matriz é', tot_impar,'\n')

    soma_colunas(matriz)

def soma_colunas(matriz):
    ''' Está função tem como objetivo somar cada uma das 5 colunas '''

    soma = 0 # Variável que realizará a soma

    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            soma += matriz[j][i]
        print('Soma dos valores da coluna ' + str(i + 1) + ': ', soma)
        soma = 0
    print()
    
    soma_linhas(matriz)

def soma_linhas(matriz):
    ''' Está função tem como objetivo somar os valores de cada uma das 5 linhas '''

    soma = 0 # Variável que realizará a soma

    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            soma += matriz[i][j]
        print('Soma dos valores da coluna ' + str(i + 1) + ': ', soma)
        soma = 0

gerar_matriz()

            