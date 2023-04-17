sexo = str(input('Qual seu sexo? ')).upper().strip()[0]



while sexo not in 'MmFf':
    sexo = str(input('Erro ! Informe seu sexo novamente: ')).upper().strip()[0]



#print('Você é um(a) {}'.format(s))
print('Sexo {} informado com sucesso !! '.format(sexo))
print('-XX'*20)

