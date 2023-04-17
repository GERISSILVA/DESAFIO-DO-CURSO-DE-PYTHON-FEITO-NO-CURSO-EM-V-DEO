#tabela do brasileirão 2022
brasileirao = ('Palmeiras','Internacional', 'Flunimense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')


print(f'Os cinco primeiro colocados no brasileirão foram: {brasileirao[0:5]}')
print(f'Os times rebaixado foram {brasileirao[16:19]}')

print(sorted(brasileirao))

print(brasileirao.index('Palmeiras'))