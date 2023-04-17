soma = 0
n = 0
cont = 0
n = int(input('Digite um número \033[31m[999 PARA PARAR ]: \033[m'))

while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número \033[31m[999 PARA PARAR ]: \033[m'))


print('Você digitou {} números e a soma entre eles foi {} '.format(cont, soma))
