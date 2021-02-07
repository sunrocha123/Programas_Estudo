def menor_nome(nomes):
    ''' Está função tem como objetivo coletar o menor nome da lista informada e devolvê-lo
        com a primeira letra maíuscula'''
    
    nome = nomes[0] # variável que receberá o menor nome

    for i in range (len(nomes)):
        if len(nomes[i].strip()) < len(nome):
            nome = nomes[i].strip()

    return nome.capitalize()

def test_answer():
    assert menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == 'José'
    assert menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == 'José'
    assert menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == 'José'
    assert menor_nome(['Bárbara', 'JOSÉ  ', 'Bill', 'Ai', 'JUDSON', ' Ana', 'OI', 'João']) == 'Ai'

