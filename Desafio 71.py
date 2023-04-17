print('=='*20)
print('BANCO DO PROGRAMADOR')
print('=='*20)

#celulas
cel = 50
totced = 0

valor = int(input('Digite o valor que você deseja  sacar: '))

total = valor 

while True:
    if total >= cel:
        total -= cel
        totced += 1
    else:
        print(f'total de {totced} cédulas de R${cel}. ')
        if cel == 50:
            cel = 20
        elif cel == 20:
            cel = 10
        elif cel == 10:
            cel = 1
        totced = 0
        if total == 0:
             break