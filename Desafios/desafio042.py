r1 = int(input('Qual a reta 1? '))
r2 = int(input('Qual a reta 2? '))
r3 = int(input('Qual a reta 3? '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Podemos formar um triângulo com essas 3 retas.')
    if r1 == r2 and r1 == r3:
        print('E esse triângulo é Equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('E esse triângulo é Isóceles!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('E esse triângulo é Escaleno!')
else:
    print('Não podemos formar um triângulo com essas 3 retas.')