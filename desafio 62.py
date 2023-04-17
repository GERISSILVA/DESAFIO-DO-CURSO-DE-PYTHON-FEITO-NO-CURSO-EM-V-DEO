pt = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
c = 0
pa = 0
t = pa
total = 0
mais = 10
usuario = 0
while mais != 0:
   total = total + mais
   while c < total:
      print('{} ->'.format(t), end=" ")
      t += razao
      c += 1

   print('PAUSA')
   mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada Foram mostrados {} termos'.format(total))
