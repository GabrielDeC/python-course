num = int(input('Digite um número de 0 a 9999: '))

numstr = str(num)

mil = numstr[0]
cen = numstr[1]
dez = numstr[2]
uni = numstr[3]

print(f'Seu número tem: \n {mil} milhar(es);\n {cen} centena(s);\n {dez} dezena(s); e\n {uni} unidade(s). ')