
soma = 0
media = 0
maioridadeh= 0
nomemaisvelho = ''
totm20 = 0
for c in range(1,5):
    print('------- {}ª PESSOA -------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
         maioridadeh = idade
         nomemaisvelho = nome
    if sexo in 'Mm' and idade> maioridadeh:
        maioridadeh= idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totm20 +=1


media = soma / 4
print('A média de idade do grupo e de {} anos '.format(media))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadeh,nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos '.format(totm20))