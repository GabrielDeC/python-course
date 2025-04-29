cid = str(input('Qual o nome da sua cidade? '))

cidupper = cid.upper()
ct = 'SANTO' in cidupper

if ct == False:
    print('Sua cidade não começa com a palavra Santo.')
else:
    print('Sua cidade começa com a palavra Santo.')
