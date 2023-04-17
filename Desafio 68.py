from random import randrange
computador = 0
cont = 0
resultado = 0
while True :
     n = int(input('Escolha :\n==================================\n1-para par \n2-para impar\n'))
     numero = int(input('Digite um número: '))
     cont += 1
     computador = (randrange(1,11) )
     resultado = numero + computador
     print(f'Número sorteado pelo computador {computador}.')
     
     if n == 1:
            if resultado % 2 != 0 :
                print('Computador ganhou!!!')
                break 
            else:
                print('Você ganhou!!! \nVamos denovo.')
     if n == 2:
            if resultado % 2 == 0:
                print('Computador ganhou!!!')
                break
            else:
                print('Você ganhou!!!!! Vamos denovo.\n')


            




