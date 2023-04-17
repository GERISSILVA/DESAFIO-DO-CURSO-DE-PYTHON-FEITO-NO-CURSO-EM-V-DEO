casa     =  float(input('Qual o valor da Casa que você que compra?'))
salario  =  float(input("Qual o valor do seu salário?"))
anos     =  int(input('Em quantos anos você pretende pagar o empréstimo ?'))

prestaçao = casa / (anos * 12)
minimo = salario * 30 /100

print ('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa ,anos),end='')
print(' A prestação será de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print( 'ESMPRESTIMO CONCEDIDO')
else:
    print('EMPRESTIMO NÃO CONCEDIDO')
