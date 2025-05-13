lista = []
escolha = 0
for i in range(0, 5):
    escolha = int(input('Escolha um número qualquer: '))
    lista.append(escolha)
    

ordem = sorted(lista)
maior = ordem[len(ordem)-1]
menor = ordem[0]
print(lista)
print(f'O maior termo da lista digitada é {maior} e o menor é {menor}. Na posição {lista.index(maior)} e na posição {lista.index(menor)}, respectivamente.')

'''for i in range(len(lista)):
    print(f'O termo {lista[i-1]} está na posição {i}, ', end='')'''
