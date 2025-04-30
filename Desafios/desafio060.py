fatorial = 1
n = c = int(input('Qual o número que você deseja calcular o fatorial? '))
print('A multiplicação a ser realizada será de: ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)
