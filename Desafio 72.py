numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezssete', 'Dezsoito', 'Dezsnove', 'Vinte')

n = int(input('Digite um número entre 0 e 20: '))
while True:
    if n <0 or n>20:
        n = int(input('Número ivalido Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número {numeros[n]}')
        break