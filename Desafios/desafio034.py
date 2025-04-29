sal = float(input('Qual seu salário atual?'))

if sal > 1250.00:
    print(f'Seu novo salário será de R$ {sal*1.1}!')
else:
    print(f'Seu novo salário será de R$ {sal*1.15}')