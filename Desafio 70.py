print('-==-'*20)
print('Loja Do Programador ')
print('-==-'*20)

soma = 0

while True:
    produto = input('Nome do produto: ')
    preco = float(input('Valor do produto: '))
    continua = input('Que continua? [S/N]:  ').upper()

    soma  += preco
    mais_barato = preco
    produto_mais_barato = produto
    produto_maiores_1000 = 0

    if continua == 'N':
        break
    if preco < mais_barato:
        mais_barato = preco
        produto_mais_barato = produto 
    if preco > 1000:
        produto_maiores_1000 += 1


print(f'\nO total gasto nas compras foi R${soma}')
print(f'O produto mais barato foi o(a) {produto_mais_barato} custando {mais_barato}')
print(f'{produto_maiores_1000} produtos custaram mais que 1000 R$. ')
    