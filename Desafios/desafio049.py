s = int(input('Qual tabuada você deseja visualizar? '))
q = int(input('Quantos números você deseja multiplicar? ')) 

for i in range(1,q+1):
    print(f'{s}x{i} = {s*i}')