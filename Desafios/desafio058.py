import random as r
import time

num = r.randint(1, 11)
adv = int()
tentativa = int()

while adv != num:
    try:
        if tentativa == 0:
            adv = int(input('Pensei em número de 1 a 10, adivinha qual é: '))
        if tentativa >= 1:
            adv = int(input('Infelizemente você não acerto, mas tente novamente: '))
        tentativa += 1
        break
    except ValueError:
        print('Ops, você digitou um texto ao invés de um número!')
        time.sleep(3)
print(f'Parabéns, acertou com {tentativa} tentativas!')
