def maximo(n1,n2, n3):
    if (n1 > n2 and n1 > n3):
        return n1
        pass
    elif (n2 > n1 and n2 > n3):
        return n2
        pass
    else:
        return n3
        pass

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
print(maximo(n1,n2, n3))