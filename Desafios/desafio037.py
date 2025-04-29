num = int(input('Digite um número inteiro: '))
base = int(input('Digite 1 para Binário \nDigite 2 para Octal \nDigite 3 para Hexadecimal \nPara qual dessas bases você deseja converter? \n '))

if base == 1:
    print(bin(num))
elif base == 2:
    print(oct(num))
elif base == 3:
    print(hex(num))