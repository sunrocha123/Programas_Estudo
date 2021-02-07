def coletaNumero():
    numeros = []
    i = True
    while i:
        digita_numero = int(input('Digite um número terminado em 0: '))
        if digita_numero == 0:
            i = False
            pass
        else:
            if digita_numero % 10 == 0:
                numeros.append(digita_numero)
                pass
            pass
    pass
    exibir(numeros)

def exibir(lista):
    tamanho = len(lista) - 1
    print("Números: ", end ="")
    while tamanho >= 0:
        if tamanho == 0:
            print(lista[tamanho], end = "")
            tamanho -= 1
            pass
        else:
            print(lista[tamanho], end = ", ")
            tamanho -= 1
            pass
        pass

print('Para finalizar o programa, digite 0')
coletaNumero()