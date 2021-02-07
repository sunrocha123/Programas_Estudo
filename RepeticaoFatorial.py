def cabecalho():
    print("===================================")
    print('LAÇOS DE REPETIÇÃO COM FATORIAL')
    print('===================================')
    print()

def executa(numero):
    fatorial = 1
    j = 2
    while j <= numero:
        fatorial = fatorial * j
        j += 1
        pass
    return fatorial

cabecalho()

i = True
while i:
    numero = int(input('Digite um número inteiro positivo: '))
    if numero == 0:
        print('O fatorial de', numero, 'é', 1)
        pass
    else:
        fatorial = executa(numero)
        print('O fatorial de', numero, 'é', fatorial)
        validarContinuacao = str(input('Deseja continuar (S/N)? '))
        if validarContinuacao == 'N' or validarContinuacao == 'n':
            i = False
            pass
        pass