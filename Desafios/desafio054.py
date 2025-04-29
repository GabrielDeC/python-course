import datetime

ano_atual = datetime.date.today().year
maiores = 0
menores = 0

for i in range(0, 7):
    nascimento = int(input('Qual o ano do seu nascimento? '))
    idade = ano_atual - nascimento
    if idade < 18:
        menores += 1
    elif idade >= 18:
        maiores += 1

print(f'Existe {maiores} pessoas maiores de idade e {menores} pessoas menores de idade.')