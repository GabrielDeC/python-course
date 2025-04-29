import random as r
item = ('Pedra', 'Papel', 'Tesoura')

comp = r.randint(0, 2)
huma = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\nQual sua escolha? '))

if comp == 0 and huma == 0:
    print('Pedra x Pedra\nEMPATE!')
elif comp == 0 and huma == 1:
    print('Pedra x Papel\nVOCÊ GANHOU!')
elif comp == 0 and huma == 2:
    print('Pedra x Tesoura\nVOCÊ PERDEU!')
elif comp == 1 and huma == 0:
    print('Papel x Pedra\nVOCÊ PERDEU!')
elif comp == 1 and huma == 1:
    print('Papel x Papel\nEMPATE!')
elif comp == 1 and huma == 2:
    print('Papel x Tesoura\nVOCÊ GANHOU!')
elif comp == 2 and huma == 0:
    print('Tesoura x Pedra\nVOCÊ GANHOU!')
elif comp == 2 and huma == 1:
    print('Tesoura x Papel\nVOCÊ PERDEU!')
elif comp == 2 and huma == 2:
    print('Tesoura x Tesoura\nEMPATE!')