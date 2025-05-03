tabela = ('Flamengo', 'Palmeiras', 'Bragantino', 'Cruzeiro', 'Fluminense', 'Internacional', 'Bahia', 'Botafogo', 'Ceará', 'São Paulo', 'Vasco', 'Corinthians', 'Juventude', 'Mirassol', 'Fortaleza', 'Vitória', 'Atlético-MG', 'Grêmio', 'Santos', 'Sport')

print('Os 5 primeiros colocados são:')
for pos in range(0, 5):
  print(f'{pos+1}. {tabela[pos]}')

print('\nOs 4 últimos colocados são:')
for z4 in range(-4, 0):
  print(f'{z4+21}. {tabela[z4]}')

print('\nA ordem alfabética dos times do brasileirão é:')
for c in sorted(tabela):
  print(f'{c};')

time = str(input('Qual time da Série A você quer saber a posição? ')).strip().lower().capitalize()
posicao = tabela.index(f'{time}') + 1
print(f'A posição do {time} está na {posicao}.')