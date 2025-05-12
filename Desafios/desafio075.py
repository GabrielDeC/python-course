a1 = a2 = a3 = a4 = 0
contagem9 = 0
posicao = 0
pares = 0
a1 = int(input('Digite um número: '))
a2 = int(input('Digite um número: '))
a3 = int(input('Digite um número: '))
a4 = int(input('Digite um número: '))

tupla = (a1, a2, a3, a4)

for i in range(0, 4):
    if tupla[i] % 2 == 0:
        pares += 1

contagem9 = tupla.count(9)
if 3 in tupla:
    posicao = tupla.index(3) + 1
    print(f'O 3 está na posição {posicao}.')
else:
    print(f'Não há o número 3 na Tupla.')

print(f'Nas suas escolhas, a tupla posssui {contagem9} números 9, tem {pares} números pares.')
