def maiusculas(frase):
    ''' Está função tem como objetivo coletar as letras maíusculas das frases '''

    lMaiusculas = '' # Está variável receberá as letras maíusculas da frase

    for i in range (len(frase)):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            lMaiusculas += frase[i]
    
    return lMaiusculas

def test_answer():
    assert maiusculas('Hoje é domingo') == 'H'
    assert maiusculas('PaTo OVO amanhã') == 'PTOVO'
    assert maiusculas('A menina GostA de cOmer BaNaNa') == 'AGAOBNN'
    assert maiusculas('PrOgRaMaMoS em python!') == 'PORMMS'