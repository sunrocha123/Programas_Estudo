def cabecalho():
    print('====================================\nREMOVENDO ELEMENTOS REPETIDOS\n====================================\n')

def remove_repetidos(lista):
    lista = sorted(lista)
    listaOrdenada = lista[:]
    for i in range(len(listaOrdenada) - 1, 0, -1):
        if listaOrdenada[i] == listaOrdenada[i - 1]:
            del lista[i - 1]
            pass
    return sorted(lista)

def coletaLista():
    lista = []
    tamanhoLista = int(input('Informe a quantidade de números que serão digitados: '))
    for i in range (tamanhoLista):
        numero = int(input('Digite um número inteiro: '))
        lista.append(numero)
    print(remove_repetidos(lista))

cabecalho()
coletaLista()