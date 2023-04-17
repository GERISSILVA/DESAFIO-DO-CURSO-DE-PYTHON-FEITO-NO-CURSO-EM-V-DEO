nota1 = int(input('Informe a primeira nota  '))
nota2 = int(input('Informe a segunda  nota  '))

print ('-'*20)
media = (nota1 + nota2) / 2

if media  >= 70 :
  print ('A media do aluno foi {} e ele aprovado !'.format(media))
elif media >=50 and media<70  :
  print ('A media do aluno foi {} e ele ficou na recuperação '.format(media))
elif media <50 :
  print ('A media do aluno foi {} e ele ficou reprovado '.format(media))