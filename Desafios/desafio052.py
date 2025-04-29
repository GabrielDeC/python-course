primo = int(input('Qual o número você deseja saber se é primo? '))
divisores = []
for i in range(1, primo+1):
    if primo%i == 0:
        divisores.append(i)
print(divisores)

if len(divisores) == 2:
    print('Esse número é primo!')
else:
    print('Esse número não é primo!')
        