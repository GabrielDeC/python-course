import random as r

a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))

array = [a1, a2, a3, a4]
esc = r.choice(array)

print(f'O aluno escolhido foi {esc}')