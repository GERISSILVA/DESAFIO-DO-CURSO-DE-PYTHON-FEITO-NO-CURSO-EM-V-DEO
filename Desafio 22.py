nome = str((input('DIGITE SEU NOME COMPLETO: '))).strip()


print('ESTAMOS ANALISANDO SEU NOME.............')
print('='*22)
print('SEU NOME SÓ COM LETRAS MAIÚSCULAS : {}'.format(nome.upper()))
print('='*22)
print('SEU NOME COM TODAS AS LETRAS EM MINÚSCULO : {} '.format(nome.lower()))
print('='*22)
print('SEU NOME TEM {} LETRAS'.format(len(nome) - nome.count(' ')))
print('='*22)
print('SEU PRIMEIRO NOME TEM {} LETRAS'.format(nome.find(' ')))
print('='*22)
