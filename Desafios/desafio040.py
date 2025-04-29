n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1+n2)/2
if media >= 7.00:
    print('APROVADO!')
elif media <= 5.00:
    print('REPROVADO!')
elif media >= 5.01 and media <= 6.99:
    print('RECUPERAÇÃO!')