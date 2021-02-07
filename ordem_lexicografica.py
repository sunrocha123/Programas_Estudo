def primeiro_lex(lista):
    ''' Está função tem como objetivo coletar o primeiro string na ordem lexicográfica '''

    string = lista[0] # Está variável guardará a string na ordem lexicográfica

    for i in range (len(lista)):
        if lista[i] < string:
            string = lista[i]

    return string


def  test_answer():
    assert primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A'
    assert primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA'