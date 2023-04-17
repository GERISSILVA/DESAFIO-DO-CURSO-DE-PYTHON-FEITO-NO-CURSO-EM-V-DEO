import random

intem = ('pedra' , 'papel' , 'tesoura')
computador = random.randint (0,2)
print('Suas opções')

print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')

jogador = int(input('QUAL SUA JOGADA ?  '))

print('JO')
print('KEN')
print('PO')
print('!')
print('>='*10)

print('O computador jogou {}'.format(intem[computador]))
print('O jogador jogou {}'.format(intem[jogador]))


print('>='*10)

if computador == 0:
    if  jogador == 0 :
        print('EMPATE!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else :
        print('Opção inválida')
elif computador == 1:
    if  jogador == 0 :
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('Opção inválida')

elif computador == 2:
    if  jogador == 0 :
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Opção inválida')

else:
    print('JOGADA INVALIDA!')
