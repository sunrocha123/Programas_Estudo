N1 = int(input('Digite o 1º número inteiro: '))
N2 = int(input('Digite o 2º número inteiro: '))
N3 = int(input('Digite o 3º número inteiro: '))
if (N1 < N2) and (N1 < N3) and (N2 > N1) and (N2 < N3) and (N3 > N1) and (N3 > N2):
    print('crescente')
    pass
else:
    print('não está em ordem crescente')
    pass