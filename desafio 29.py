
vel = float(input('Qual e a velocidade do carro? '))
if vel >80:
    print('MULTADO! Você execedeu o limite permitido de 80/km ')
    multa = (vel-80) * 7
    print('O valor da multa e de R${:.2f}!'.format(multa))
print('Tenha um exelente dia e DIRIJA COM CUIDADO! ')

