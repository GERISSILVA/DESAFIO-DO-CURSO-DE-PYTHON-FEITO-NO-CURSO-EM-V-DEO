salario = float(input('Informe seu Salário : '))
if salario <= 1250:
    salario1 = salario + (salario * 15 /100)
    print('O salario antes era {} agora  e : {:.2f}'.format(salario,salario1))
else:
    salario1 = salario + (salario * 10 / 100)
    print('O salario antes era {} agora  e : {:.2f}'.format(salario,salario1))