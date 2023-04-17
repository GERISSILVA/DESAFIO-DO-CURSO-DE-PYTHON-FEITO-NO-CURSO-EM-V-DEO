

homens = 0
pessoas_maiores_q_18 = 0
mulheres_menores_q_20 = 0

while True:
    idade = int(input('Qual sua idade? '))
    sexo  = input('Digite o sexo [M/F]: ')
    continua = input('Que continua? [S/N]: ').upper()

    if sexo == 'm' :
        homens += 1
    if idade > 18 :
        pessoas_maiores_q_18 += 1
    if sexo == 'f' :
            if idade <20:
                mulheres_menores_q_20 += 1
    
    if continua == 'N' :
        break
    
print(f'Foram cadastrados {homens} homens. ')
print(f'Foram cadastradas {pessoas_maiores_q_18} pessoas maiores que 18 anos. ')
print(f'Foram cadastradas {mulheres_menores_q_20} mulheres com menos de 20 anos. ')
