import random
cont = 0
sorteio = random.randint(0,10)
print('VAMOS JOGARRRRR!!!')
num = int(input('Tente acerta o número que vou sortea entre 0 e 10: '))
while sorteio != num:
    num = int(input('ERROU!! , tente Novamente : '))
    cont += 1
print('Parabéns você acertou!!!!!')
print('Você tentou {} vezes para acerta '.format(cont))