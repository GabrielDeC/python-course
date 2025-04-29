a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))

if a > b and a > c:
    print(f'O número {a} é o maior número!')
elif b > a and b > c:
    print(f'O número {b} é o maior número!')
else:
    print(f'O número {c} é o maior número!')