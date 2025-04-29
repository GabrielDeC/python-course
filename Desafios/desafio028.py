import random as r

num = r.randint(1, 5)

adv = int(input('Pensei em número de 1 a 5, adivinha qual é: '))

if num == adv:
    print('Parabéns, acertou!')
else:
    print('Erroooooouuuuu! Tente novamente!')
print(num)