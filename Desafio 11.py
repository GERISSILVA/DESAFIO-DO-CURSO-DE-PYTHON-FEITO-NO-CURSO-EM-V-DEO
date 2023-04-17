altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(altura,largura,altura*largura))
print('Você vai gastar {:.2f} litros de tinta'.format((altura*largura)/2))