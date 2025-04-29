nome = str(input('Qual seu nome completo? '))

anome = nome.split()
qtd = len(anome) - 1

print(f'Seu primeiro nome é {anome[0]}\n Seu último nome é {anome[qtd]}')
