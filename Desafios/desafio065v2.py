n = cont = soma = maior = menor = 0
lista = []
valid = ''
while valid in 'S':
    if cont == 0:
        n = int(input('Digite um número qualquer: '))
    if cont > 0:
        valid = str(input('Deseja continuar digitando [S ou N]? '))
        if valid == 'S':
            n = int(input('Digite outro número: '))
    cont += 1
    soma += n
    lista.append(n)
    print(lista)

print(f'A média de todos os números digitados é {soma/cont} e o maior número é {max(lista)} e o menor número é {min(lista)}.')
