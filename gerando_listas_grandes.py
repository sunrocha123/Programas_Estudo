import random

def lista_grande(n):
    lista = []

    if type(n) == float:
        return False
    else:
        for i in range (n):
            numero = random.randint(-999, 999)
            lista.append(numero)
        return lista


if __name__ == "__main__":

    print(lista_grande(-2))
    print()
    print(lista_grande(67))
    print()
    print(lista_grande(3.2))
