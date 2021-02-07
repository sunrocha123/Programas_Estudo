i = True
while i:
    n = int(input("Digite um número inteiro maior que 1: "))
    if n == 2 or n == 3 or n == 5 or n == 7:
        print('primo')
        i = False
        pass
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        print('não primo')
        pass
    else:
        print('primo')
        i = False
        pass
    pass