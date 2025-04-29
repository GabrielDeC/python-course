from math import sqrt

co = float(input('Qual o comprimento do Cateto Oposto? '))
ca = float(input('Qual o comprimento do Cateto Adjacente? '))

h = sqrt(ca**2 + co**2)

print(f'O valor da hipotenusa é {h}')