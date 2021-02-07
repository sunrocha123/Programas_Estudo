def cabecalho():
    print('===============================\nINVERTENDO SEQUÊNCIA\n===============================\n')

def ordem_inversa(lista):
    k = len(lista) - 1
    while k >= 0:
        print(lista[k])
        k -= 1
        pass

def coletaLista():
    lista = []
    i = True
    print('Para finalizar o programa, digite 0')
    while i:
        numero = int(input('Digite um número inteiro: '))
        if numero == 0:
            i = False
            pass
        else:
            lista.append(numero)
            pass
        pass
    ordem_inversa(lista)

cabecalho()
coletaLista()