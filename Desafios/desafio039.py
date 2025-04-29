import datetime
ano = int(input('Em que ano você nasceu? '))
atual = datetime.date.today().year

if (atual - ano) == 18:
    print('Estamos no ano que você deve se alistar. ALISTE-SE')
elif (atual - ano) < 18:
    print(f'Ainda não estamos no ano que você deve se alistar. Faltam apenas {18 - (atual - ano)} anos para isso.')
elif (atual - ano) > 18:
    print(f'Já passamos do ano que você deve se alistar. Passaram-se {atual - ano - 18} anos do seu alistmento')
