from datetime import date
data = date.today().year
menor = 0
maior = 0
for pessoas in range(1,8) :
    nasc = int(input('Quantos anos a {}ª pessoa nasceu ? '.format(pessoas)))
    idade = data - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1


print('{} pessoas são de maior idade '.format(maior))
print('{} pessoas são de menor idade '.format(menor))