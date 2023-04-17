import math
oposto = float(input('INFORME O CATETO OPOSTO DO TRIANGULO RETANGULO: '))
adj = float(input('INFORME O CATETO ADJACENTE DO TRIANGULO RETANGULO: '))
ipoten = math.hypot(oposto,adj)
print('O CATETO OPOSTO DO TRIANGULO    E = {}'.format(oposto))
print('O CATETO ADJACENTE DO TRIANGULO E = {}'.format(adj))
print('A HIPOTENUSA DO TRIANGULO       E = {:.2f}'.format(ipoten))