casa = float(input('Qual o valor da casa em R$? '))
sal = float(input('Qual o seu salário em R$? '))
temp = int(input('Em quanto tempo você pretende pagar a casa? '))
months = temp*12

if (casa/months)/sal < 0.3:
    print(f'O seu crédito foi aprovado e sua parcela inicial será de R$ {casa/months:.5}!')
else:
    print(f'Infelizmente seu crédito não foi aprovado :/')