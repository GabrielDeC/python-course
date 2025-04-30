a1 = int(input('Diga o primeiro termo da sua PA: '))
r = int(input('Qual a razão da sua progressão? '))
termos = int(input('Quantos termos você deseja armazenar? '))

print('Podemos dizer que os termos da sua PA são: ', end='')

while termos > 0:
    print(f'{a1}', end='')
    print(', ' if termos > 1 else '.\n', end='')
    a1 = a1 + r
    termos -= 1
