n = int()
tabuada = 1

while True:
    n = int(input('Qual número deseja saber a tabuada? '))
    if n > 0:
        for tabuada in  range(1, 11):
            print(f'{n} x {tabuada} = {n*tabuada}')
            tabuada += 1
    else:
        break
