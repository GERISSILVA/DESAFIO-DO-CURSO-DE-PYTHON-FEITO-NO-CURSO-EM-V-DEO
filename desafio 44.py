valor = float(input('Qual o valor a ser pago R$? '))

('FORMAS DE PAGAMENTOS ')
print('[1] A vista dinheiro/cheque ')
print('[2] A vista no cartão')
print('[3] 2x no cartão ')
print('[4] 3x ou mais no cartão ')
escolha = int(input('Qual a opção ? '))

print('')

print('LOJA DE INFORMATICA DE GERIS -__-')

print('')


if escolha == 1  :
   vfinal = valor - valor * (10/100) 
   print('O valor a ser pago e R${} vai custar R${} no final. '.format(valor,vfinal))
elif escolha == 2:
   vfinal = valor - valor * (5/100)
   print('O valor a ser pago e R${} vai custar R${} no final .'.format(valor,vfinal))
elif escolha == 3:
   vfinal = valor // 2
   print('Sua compra será parcelada 2 x de {} no cartão sem juros '.format(valor,vfinal))
elif escolha == 4:
   parcela = int(input('Em quantas vezes você que dividi a compra ? '))
   vfinal = valor + valor *(20/100)
   total = vfinal // parcela
   print('')

   print('Sua compra será parcelada em {}x de {} COM JUROS. '.format(parcela,total))
   print('Sua compra de R${} vai ficar de R${} no final'.format(valor,vfinal))
else:
   print('ERRO NO PROCESSO ')