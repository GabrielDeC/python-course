vel = float(input('Insira a velocidade medida em km/h: '))

if vel > 80:
    multa = (vel-80)*7
    print(f'Você excedeu o limite de velocidade e foi multado em R$ {multa}!')
else:
    print('Parabéns, você não excedeu o limite de velocidade!')
