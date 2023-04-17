num = int(input('Qual número deseja ver a fatorial ?  '))

fatorial = 1
cont = num
print('Calculando fatorial de  {}! = '.format(num), end=' ')
while cont > 0:
     print(cont, end=' ')
     fatorial *= cont
     cont -= 1
     print('x' if cont > 1 else '=', end=' ')

print(fatorial)
