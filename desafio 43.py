peso = float(input('Qual e seu peso (kg)? '))
altura = float(input('Qual sua altura (m)? '))

imc = peso / ( altura**2) 

if imc <18.5 :
    print ('O IMC dessa pessoa e {:.1f} e ela está abaixo do peso'.format(imc))
elif imc == 18.5 <=24.9:
    print('O IMC dessa pessoa e {:.1f} e está normal! '.format(imc))
elif imc ==25 <=29.9 :
    print('O IMC dessa pessoa e {:.1f} e ela esta acima do peso'.format(imc))
elif imc ==30 <=34.9 :
    print('O IMC dessa pessoa e {:.1f} e ela está Obeso de grau I'.format(imc))
elif imc ==35 <39.9:
    print('O IMC dessa pessoa e {:.1f} e ela está obeso de grau II'.format(imc))
elif imc >40 :
    print('O IMC dessa pessoa e {:.1f} e ela está obeso de grau III'.format(imc))