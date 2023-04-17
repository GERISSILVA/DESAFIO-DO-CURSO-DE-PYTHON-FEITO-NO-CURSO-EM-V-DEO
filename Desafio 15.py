dias = int(input('Quantos dias ele foi alugado? '))
km = float(input('Quantos km foi percorrido pelo carro? '))

precod = dias*60
precokm = km*0.15
valortotal = precod+precokm
print('-'*25)
print('Você rodou {} dias e vai pagar: R${}'.format(dias, precod))
print('Você rodou {} km e vai pagar: R${:.2f}'.format(km, precokm))
print("VOCE VAI PAGAR NO TOTAL DE:     R${}".format(valortotal))
print('-'*25)


