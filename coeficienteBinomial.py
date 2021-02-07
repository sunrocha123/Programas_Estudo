import math

# exibição do cabeçalho

def cabecalho():
    print("===================================")
    print("CÁLCULO DO COEFICIENTE BINOMIAL")
    print("===================================")
    print('')

# cálculo do coeficiente binomial

def coeficienteBinomial(n, p):
    calculo = math.factorial(n)/(math.factorial(p) * math.factorial(n - p))
    return calculo

cabecalho()

n = int(input("Digite o valor de n: "))
p = int(input("Digite o valor da classe p: "))
while n <= p:
    print('O valor de n, precisa ser maior ou igual a p')
    n = int(input("Digite o valor de n: "))

print("O valor do coeficiente binomial é", coeficienteBinomial(n, p))
