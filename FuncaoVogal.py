def vogal(letra):
    if (letra == "a" or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
        return True
        pass
    elif (letra == "A" or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):
        return True
        pass
    else:
        return False
        pass

letra = str(input("Digite uma letra: "))
print(vogal(letra))