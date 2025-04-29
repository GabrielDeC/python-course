l = float(input('Qual a largura em Metros da parede? '))
al = float(input('Qual a altura em Metros da parede? '))
t = float(input('Qual área um balde de tinta pinta? '))

print('Sendo assim, é necessário {:.2f} baldes de tinta para pintar essa parede.'.format(float((l*al)/t)))
