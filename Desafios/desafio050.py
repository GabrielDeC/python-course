n = 0
for i in range(0,6):
    s = int(input('Qual número deseja somar? '))
    if s%2 == 0:
        n = s + n
print(f'A soma dos números pares é {n}')