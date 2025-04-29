import datetime

ano = int(input('Qual ano de nascimento do nadador? '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano

if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <=14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade == 20:
    print('Master')
elif idade > 20:
    print('Sênior')