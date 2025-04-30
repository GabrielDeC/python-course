a1 = int(input('Diga o primeiro termo da sua PA: '))
r = int(input('Qual a razão da sua progressão? '))
cont = 1
adicional = int(input('Quantos termos você deseja visualizar? '))
total = 0
print('Podemos dizer que os termos da sua PA são: ', end='')

while adicional != 0:
    total = total + adicional
    while cont <= total:
        print(f'{a1} -> ', end='')
        a1 += r
        cont += 1
    print('Fim')
    adicional = int(input('Quantos termos adicionais deseja colocar? '))
print(f'Fim da sequência com {total} termos.')