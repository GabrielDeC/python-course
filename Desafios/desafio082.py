lista = []
listaPares = []
listaImpares = []
numero = 0
continuar = 0
while True:
    numero = int(input('Digite um número a ser adicionado: '))
    lista.append(numero)
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)
    continuar = str(input('Deseja continuar adicionando (S/N)? '))
    if 'N' in continuar:
        break

print(lista)
print(listaPares)
print(listaImpares)