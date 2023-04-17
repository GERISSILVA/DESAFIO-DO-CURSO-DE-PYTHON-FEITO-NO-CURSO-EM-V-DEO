from datetime import date 
atual = date.today().year

ano = int(input('Informe o ano de nascimento : '))
idade = atual - ano

print("Quem nasceu em {} tem {} anos em {} ".format(ano , idade , atual ))



if idade == 18 :
    print ( 'Você ja pode se alistar ao execito ')
elif idade > 18: 
    print('Você já podia te se alistado a {} anos '.format(idade - 18))
elif idade <18 :
    print ('Falta {} anos para você se alista'.format(idade - 18))