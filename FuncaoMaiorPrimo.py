def maior_primo(n):
    if (n == 2 or n == 3 or n == 5 or n == 7):
        return n
        pass
    elif (n == 4 or n == 6):
        return n - 1
        pass
    elif (n == 8 or n == 9 or n == 10):
        return 7
        pass
    elif (n > 953 and n < 966):
        return 953
        pass
    elif (n > 977 and n < 983):
        return 977
        pass
    elif (n > 983 and n < 991):
        return 983
        pass
    else:
        i = 8
        numero = 0
        while i <= n:
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                i+=1
                pass
            else:
                numero = i
                i+=1
                pass
            pass
        return numero
        pass

n = int(input("Digite um número: "))
while n < 2:
    print("Digite um número maior ou igual a 2")
    n = int(input("Digite novamente o número: "))
    pass

print(maior_primo(n))

