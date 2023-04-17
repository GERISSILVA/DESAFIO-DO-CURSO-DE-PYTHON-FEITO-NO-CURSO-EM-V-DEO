n1 = int(input('DIGITE UM NÚMERO: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
n = n1 // 1000 % 10
print('Analisando o número {}'.format(n1))
print('UNIDADE: {}'.format(u))
print('DEZENA : {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR : {}'.format(n))

