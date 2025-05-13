lista = []
unico = []
valor = 0
continuar = ''

while True:
    valor = int(input('Qual o valor a ser adicionado na lista? '))
    lista.append(valor)
    print('O Valor foi adicionado com sucesso...')
    continuar = str(input('Deseja continuar adicionando (S/N)? ')).strip().upper()
    if 'N' in continuar:
        break

for i in range(len(lista)):
    if i == 0:
        unico.append(lista[i])
    if i >= 1:
        if lista[i] not in unico:
            unico.append(lista[i])

print(f'Você digitou em números únicos os seguintes números: {sorted(unico)}.')