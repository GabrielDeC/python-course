n = cont = soma = maior = menor = 0
valid = ''
while valid in 'S':
    n = int(input('Digite um número qualquer: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    valid = str(input('Você deseja continuar com a listagem de números? [S ou N]')).upper().strip()

print(f'A média de todos os números digitados é {soma/cont} e o maior número é {maior} e o menor número é {menor}.')
