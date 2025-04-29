a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))

for i in range (0,10):
    print(f'O termo {i+1} é {a1 + r*i}!')