n1 = int(input('Informe-me um número :  '))

print('------- ESCOLHA UMA CONVERSÃO -------')
print('1 PARA BINÁRIO')
print('2 PARA OCTAL  ')
print('3 PARA HEXADECIMAL')

conversao = int(input('  Sua opção  '))

if conversao == 1 :
    print ('{} convertido para binario é ingual a {}'.format(n1, bin(n1)))
elif conversao == 2:
    print('{} convertido para OCTAL é ingual a {} '.format(n1, oct(n1)))
elif conversao == 3:
    print ('{} convertido para HEXADECIMALA é ingual {}'.format(n1,  hex(n1)))