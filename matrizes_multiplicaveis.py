def sao_multiplicaveis(m1, m2):
    for i in range(len(m1)):
        if len(m1[i]) != len(m2):
            return False
            pass
        else:
            return True
            pass


def test_answer():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    m3 = [[1], [2], [3]]
    m4 = [[1, 2, 3]]
    assert sao_multiplicaveis(m1,m2) == False
    assert sao_multiplicaveis(m3,m4) == True