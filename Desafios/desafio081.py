lista = []
numero = 0
contagem = 1
continuar = ''
while True:
    numero = int(input('Digite um número a ser adicionado: '))
    lista.append(numero)
    continuar = str(input('Deseja seguir adicionando (S/N)? ')).strip().upper()
    contagem += 1
    if 'N' in continuar:
        break

lista.sort(reverse=True)
print(f'A quantidade de dados inseridos foram: {contagem}.')
print(f'O dados inseridos foram: {lista}')
print('O número 5 foi digitado!' if 5 in lista else 'O número 5 não foi digitado!' )