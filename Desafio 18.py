import math
angulo = int(input('INFORME O ÃNGULO QUE VOCÊ DESEJA: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ANGULO E {}'.format(angulo))
print('O SENO E {:.2f}'.format(seno))
print('O COSENO E {:.2f}'.format(cos))
print('A TANGENTE E {:.2f}'.format(tan))
