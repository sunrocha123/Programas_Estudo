numeroAdjacentesIguais = False
while not numeroAdjacentesIguais:
    numero = input("Digite um número: ")
    numeroAlteradoInteiro = 0
    numeroAlteradoResto = 0
    i = 0
    while i <= len(numero) and not numeroAdjacentesIguais:
        if i == 0:
            RestoDivisao = int(numero) % 10
            DivisaoInteira = int(numero) // 10
            numeroAlteradoInteiro = DivisaoInteira
            numeroAlteradoResto = RestoDivisao
            i += 1
            pass
        elif i == len(numero):
            print("não")
            break
            pass
        else:
            RestoDivisao = numeroAlteradoInteiro % 10
            DivisaoInteira = numeroAlteradoInteiro // 10
            if numeroAlteradoResto == RestoDivisao:
                numeroAdjacentesIguais = True
                print("sim")
                break
                pass
            numeroAlteradoInteiro = DivisaoInteira
            numeroAlteradoResto = RestoDivisao
            pass
            i += 1
        pass