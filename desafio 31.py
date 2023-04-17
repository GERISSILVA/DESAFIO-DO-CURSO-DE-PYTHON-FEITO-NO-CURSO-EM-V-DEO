preco = float(input('Qual a distância da viagem em km? '))
if preco <= 200:
    viagem = preco * 0.50
    print('Com a distância de {} km o valor da viagem ficará {:.2f} .'.format(preco , viagem))

else:
    viagem = preco * 0.45
    print ('Com a distância de {} km o valor da viagem ficará R${:.2f} . '.format(preco , viagem))