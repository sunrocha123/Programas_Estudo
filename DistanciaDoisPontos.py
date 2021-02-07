N1 = float(input('Digite o 1º número: '))
N2 = float(input('Digite o 2º número: '))
N3 = float(input('Digite o 3º número: '))
N4 = float(input('Digite o 4º número: '))

#N1 e N2 são as coordenadas do ponto 1 no plano cartesiano
#N3 e N4 são as coordenadas do ponto 2 no plano cartesiano

#ponto 1

x1 = N1
y1 = N2

#ponto 2

x2 = N3
y2 = N4

import math
DistanciaEntrePontos = math.sqrt(((x1 - x2)**2) + ((y1 - y2)** 2))

if DistanciaEntrePontos >= 10:
    print('longe')
    pass
else:
    print('perto')
    pass