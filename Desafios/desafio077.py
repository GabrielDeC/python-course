palavras = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as seguintes vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()}, ', end='')
