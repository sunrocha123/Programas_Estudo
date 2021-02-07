def cabecalho():
    print('======================================\nMAIOR ELEMENTO DE UMA LISTA\n======================================\n')

def maior_elemento(lista):
    maiorElemento = 0
    if len(lista) == 1:
        return lista[0]
        pass
    else:
        k = len(lista) - 1
        while k >= 0:
            if lista[k] > lista[k - 1]:
                if lista[k] > maiorElemento and lista[k] > 0:
                    maiorElemento = lista[k]
                    pass
                elif lista[k] < 0 and maiorElemento == 0:
                    maiorElemento = lista[k]
                    pass
                pass
            k -= 1
            pass
    return maiorElemento
    pass
def coletaLista():
    lista = []
    tamanhoLista = int(input('Informe a quantidade de números que serão digitados: '))
    for i in range(tamanhoLista):
        numero = int(input('Digite um número inteiro: '))
        lista.append(numero)
    print(maior_elemento(lista))

cabecalho()
coletaLista()