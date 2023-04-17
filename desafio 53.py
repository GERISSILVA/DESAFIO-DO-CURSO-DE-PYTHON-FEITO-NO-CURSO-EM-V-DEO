frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split()
junto =  ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]

if inverso == junto:
    print('A frase é um Palindromo')
else:
    print('A frase não é Palindromo')
print('Sua frase : \033[31m{}'.format(frase))
print('\033[mInverso da sua frase : \033[31m {} '.format(inverso))