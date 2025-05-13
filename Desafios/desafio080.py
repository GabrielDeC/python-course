lista = []
numero = 0
for i in range(0, 5):
    numero = int(input('Qual o valor a ser inserido? '))
    if i == 0 or numero > lista[-1]:
        lista.insert(i, numero)
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                break
            posicao += 1

print(lista)
