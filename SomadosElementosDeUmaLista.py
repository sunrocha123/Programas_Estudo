def cabecalho():
    print('===================================\nSOMA DOS ELEMENTOS DE UMA LISTA\n===================================\n')

def soma_elementos(lista):
    totSoma = 0
    for i in range(len(lista)):
        totSoma += lista[i]
    return totSoma

def coletaLista():
    tamanhoLista = int(input('Informe a quantidade de números que serão digitados: '))
    lista = []
    for i in range (tamanhoLista):
        numero = int(input('Digite um número inteiro: '))
        lista.append(numero)
    print(soma_elementos(lista))

cabecalho()
coletaLista()