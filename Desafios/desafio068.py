import random as r

n = 0
computador = int()
jogador = int()

while True:
    jogador = int(input('Qual seu número para jogar? '))
    computador = r.randint(0, 10)
    jog_parimpar = int(input('Par [1] ou Ímpar [2]? '))
    soma = computador + jogador
    print(f'A sua jogada foi de {jog_parimpar} e a do computador foi {computador}.')
    if jog_parimpar == 1 and soma % 2 == 0:
        print('Você ganhou!')
        n += 1
    elif jog_parimpar == 2 and soma % 2 != 0:
        print('Você ganhou!')
        n += 1
    else:
        print(f'Infelizmente você perdeu! Sua sequência de vitórias foi de {n}!')
        break
