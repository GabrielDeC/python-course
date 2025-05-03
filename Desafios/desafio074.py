import random as r

a1 = a2 = a3 = a4 = a5 = maior = menor = int()
a1 = r.randint(0,100)
a2 = r.randint(0,100)
a3 = r.randint(0,100)
a4 = r.randint(0,100)
a5 = r.randint(0,100)

tupla = (a1, a2, a3, a4, a5)

for i in range(0, 5):
  if i == 0:
    maior = menor = tupla[i]
  if i > 0:
    if tupla[i] > maior:
      maior = tupla[i]
    if tupla[i] < menor:
      menor = tupla[i]

print(maior)
print(menor)
print(tupla)