import random
alun1 = str(input('Informe o nome do aluno: '))
alun2 = str(input('Informe o nome do aluno: '))
alun3 = str(input('Informe o nome do aluno: '))
alun4 = str(input('Informe o nome do aluno: '))
sorteio = [alun1, alun2, alun3, alun4]


random.shuffle(sorteio)
print("-"*20)
print('A ORDEM DE APRESENTAÇÃO E :')
print(sorteio)

