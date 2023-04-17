
n = int(input('Informe um número : '))
tot=0
for c in range(1, n + 1):
     if  n % c == 0:
         # print('O número e primo e foi dividido {} vezes '.format(cont))
         print('\033[33m', end=' ')
         tot+=1
     else:
         # print('O Número não e primo foi dividido mais de duas vezes@!!!')
         print('\033[31m', end=' ')
     print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes '.format(n,tot))
if tot ==2:
     print('É Por isso que ele e um número primo')
else:
     print('Éz  por isso ele não e um númeor primo!')
    # else:
          #print('\033[33', end= ' ')


     