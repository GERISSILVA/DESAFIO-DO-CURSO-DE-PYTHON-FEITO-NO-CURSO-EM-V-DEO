#obs foi uma amiga depresiva q mandou essas palavras 
palavras = ('Corte', 'Estileite', 'Roupa', 'Dinheiro', 'Amor', 'Decepçao')

for prox in palavras : 
    print(f'\nNa palavra {prox.upper()} temos as vogais ', end='')
    for letra in prox:
        if letra.lower() in 'aeiou':
            print( letra , end=' ')

