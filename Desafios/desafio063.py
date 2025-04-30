n = int(input('Quantos número de fibonacci você deseja visualizar? '))
a1 = 0
a2 = 1
fim = 3
print(f'A sequência de fibonacci solicitada é: {a1} -> {a2} -> ', end='')
while fim <= n:
    a3 = a2 + a1
    print(f'{a3} -> ', end='')
    a1 = a2
    a2 = a3
    fim += 1
print('Encerraram os termos.')