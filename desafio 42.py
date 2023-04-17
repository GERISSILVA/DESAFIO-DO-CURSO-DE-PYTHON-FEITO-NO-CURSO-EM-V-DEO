lado1 = int(input('Qual o valor do primeiro segmento do triangulo? '))
lado2 = int(input('Qual o valor do segundo segmento do triangulo? '))
lado3 = int(input('Qual o valor do terceiro segmento do triangulo? '))



if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3< lado1 + lado2:
    print('As retas podem fazer um triângulo ', end= '')
    if lado1 == lado2 and lado1 == lado3 :
     print('EQUILÁTERO!')
    elif lado1 == lado2 :
      print('ISOSCELES!')
    elif lado1 == lado3:
      print('ISOSCELES!')
    elif lado2 == lado3 :
      print('ISOSCELES!')
    elif lado1 != lado2 != lado3 != lado1 :
     print ('ESCALENO!')

else:
    print('Não e possivel formar um triângulo com essa retas !')
