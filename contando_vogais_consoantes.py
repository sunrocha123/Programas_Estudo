def conta_letras(frase, contar="vogais"):
    ''' Está função tem como objetivo contar a quantidade de vogais ou consoantes
        da frase apresentada '''

    vogais = ['a','e','i','o','u']
    tot_vogais = 0 # Variável que receberá o total de vogais que possui na frase
    tot_consoantes = 0 # Variável que receberá o total de consoantes que possui na frase

    if contar == "vogais":

        for i in range (len(frase)):
            if frase[i] in vogais:
                tot_vogais += 1

        return tot_vogais

    else:

        for i in range (len(frase)):
            if frase[i] not in vogais and frase[i] != " ":
                tot_consoantes += 1

        return tot_consoantes

def test_answer():

    assert conta_letras('programamos em python') == 6
    assert conta_letras('programamos em python', 'vogais') == 6
    assert conta_letras('programamos em python', 'consoantes') == 13

