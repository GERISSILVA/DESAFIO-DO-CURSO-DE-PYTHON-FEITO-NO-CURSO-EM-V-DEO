cont = 0
soma = 0
media = 0
maior = 0
menor = 0
#n = int(input('Digite um número: '))
resposta = 'S'
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    resposta = str(input('Que continuar? [N/S]')).upper()

    media = soma / cont
    if cont == 1:
        maior = n
        menor = n

    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
print('Foram informados {} números e a média foi de {}'.format(cont, media))
print('O maior número foi {} e o menor foi {}.'.format(maior, menor))
