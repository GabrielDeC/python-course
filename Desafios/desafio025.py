cid = str(input('Qual seu nome completo? '))

cidupper = cid.upper()
ct = 'SILVA' in cidupper

if ct == False:
    print('Seu nome não tem Silva.')
else:
    print('Seu nome tem Silva.')