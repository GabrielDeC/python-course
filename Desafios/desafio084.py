lista = list()
preenchimento = list()
continuar = ''
maiorPeso = menorPeso = int()
while True:
    preenchimento.append(str(input('Nome: ')))
    preenchimento.append(float(input('Peso: ')))
    if len(lista) == 0:
        maiorPeso = menorPeso = preenchimento[1]
    else:
        if preenchimento[1] > maiorPeso:
            maiorPeso = preenchimento[1]
        if preenchimento[1] < menorPeso:
            menorPeso = preenchimento[1]
    lista.append(preenchimento[:])
    preenchimento.clear()
    continuar = str(input('Deseja continuar adicionando (S/N)? ')).strip().upper()
    if continuar in 'N':
        break

print()
print(f'Foram registrados {len(lista)} {'informações' if len(lista) > 0 else 'informação'}.')
print(f'O maior peso foi {maiorPeso} Kg. Peso de ', end='')
for i in lista:
    if i[1] == maiorPeso:
        print(f'{i[0]} ', end='')
print()

print(f'O menor peso foi {menorPeso} Kg. Peso de ', end='')
for i in lista:
    if i[1] == menorPeso:
        print(f'{i[0]} ', end='')
print()
