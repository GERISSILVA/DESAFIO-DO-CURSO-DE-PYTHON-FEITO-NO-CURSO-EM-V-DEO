import random
print('SORTEIO')
print(35*'-')
resul = (int(input('!! De 0 a 5 tente advinha no número que eu vou pensar !!  ')))
print(35*'-')
num=random.randint(0,5)

if resul == num:
    print('VOCÊ GANHOU -_-!')
else:
    print('GANHEI! eu pensei no número {} não no {} '.format(num,resul))