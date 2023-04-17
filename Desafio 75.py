
n = (int(input('Digite um valor:')),
     int(input('Digite um valor:')),
     int(input('Digite um valor:')),
     int(input('Digite um valor:')))

print(f'Você digitou os seguintes números {n}')

#verificando o numero 9

if 9 in n:
    print(f'O valor 9 apareceu na posição {n.index(9)}') 
else:
    print('Não foi informado o número 9')

#verificando o número 3

if 3 in n:
    print(f'O valor 3 apareceu na posição {n.index(3)}')
else:
    print('Não foi informado o número 3')

#verificando os números pares

print(f'Os valores pares digitados foram :', end='')
for numero in n:
    if numero % 2 == 0:
        print(',',numero, end=' ')
