numero1 = int()
numero2 = int()
escolha = int()

while escolha != 5:
    numero1 = int(input("Escolha o primeiro número: "))
    numero2 = int(input("Escolha o segundo número: "))
    escolha = int(input("[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair \nEscolha qual a operação a ser realizada: "))
    if escolha == 1:
        print(f'A soma é {numero1 + numero2}')
    if escolha == 2: 
        print(f'A multiplicação é {numero1 * numero2}')
    if escolha == 3:
        if numero1 > numero2: 
            print(f'O maior é {numero1}')
        else:
            print(f'O maior é {numero2}')
if escolha == 5: 
    print('Agradeço sua participação!')