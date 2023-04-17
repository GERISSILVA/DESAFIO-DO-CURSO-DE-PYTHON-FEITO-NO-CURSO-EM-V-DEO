print('=+'*20)

primeirot = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))

print('=+'*20)
termo =  primeirot + (10-1) * razao
for c in range ( primeirot, termo + razao,  razao):
    
    print  ( ' {} '.format(c), end=' -> ' )
    
    
print('ACABOU')    

print('=+'*20)

