n = int()
cont = 0
soma = 0

while n != 999:
    if cont == 0:
        n = int(input('Digite um número qualquer: '))
    if cont > 0:
        n = int(input('Digite outro número e caso deseja parar, digite 999: '))
    soma += n
    cont += 1

print(f'A soma de todos os números digitados é {soma - 999} e forma {cont-1} números digitados.')