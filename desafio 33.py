num  = int(input('Informe um número : '))
num2 = int(input('Informe outro número : '))
num3 = int(input('Informe o terceiro número : '))
#vendo qual menor
menor = num

if num2<num3 and num2<num:
    menor=num2
if num3<num and num3<num2:
    menor = num3

#vendo qual maior
maior = num
if num2>num3 and num2>num:
    maior=num2
if num3>num and num3>num2:
    maior = num3

print(40*"-")
print('O maior número e {}'.format(maior))
print('O menor número e {}'.format(menor))