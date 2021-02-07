def cabecalho():
    print("============================")
    print('QUANTIDADE DE PRIMOS')
    print('============================')
    print()

def n_primos(x):
    i = 2
    fator = 2
    quantPrimos = 0
    if i == 2:
        quantPrimos += 1
        i += 1
        pass
    while i <= x:
        while i % fator != 0 and fator <= i/2:
            fator += 1
            pass
        if i % fator == 0:
            i += 1
            fator = 2
            pass
        else:
            quantPrimos += 1
            i += 1
            fator = 2
            pass
        pass
    return quantPrimos

cabecalho()

numero = int(input("Digite um número inteiro maior ou igual a 2: "))
print(n_primos(numero))

