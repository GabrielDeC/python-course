lista = ('Lapis', 2, 'borracha', 1.59, 'caderno', 2.52)

for posicao in range(0, len(lista)):
    if posicao % 2 ==0:
        print(f'{lista[posicao]:.<30}', end='')
    else:
        print(f'R$ {lista[posicao]:>2.2f}')
