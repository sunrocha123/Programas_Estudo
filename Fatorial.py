n = int(input("Digite um número natural: "))
fat = 1
i = 2
if n == 0:
    print(1)
    pass
else:
    while i <= n:
        fat = fat * i
        i += 1
        pass
    print(fat)
    pass

