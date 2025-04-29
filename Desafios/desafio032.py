ano = int(input('Em que ano estamos? '))

if ano%4 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')