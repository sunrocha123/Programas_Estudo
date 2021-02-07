def cabecalho():
    print('=============================')
    print('IMPRIMIR UM RETÂNGULO')
    print('=============================')
    print()

def executa(largura, altura):
    i = 1
    while i <= altura:
        if i == 1 or i == altura:
            j = 1
            while j <= largura:
                print("#", end = "")
                j += 1
                pass
            print()
            i += 1
            j = 1
            pass
        else:
            k = 2
            print("#", end = "")
            while k < largura:
                print(" ", end = "")
                k += 1
                pass
            print("#", end = "")
            print()
            i += 1
            k = 2
            pass
        pass

def dados():
    largura = int(input('Digite a largura de um retângulo maior que 0: '))
    altura = int(input('Digite a altura de um retângulo maior que 0: '))
    executa(largura, altura)

cabecalho()
dados()