pt = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
c = 0
pa = 0
t = pt
while c < 10:
   print('{} ->'.format(t), end=" ")
   t += razao
   c += 1

print('FIM')