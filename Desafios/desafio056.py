# Definição de Variáveis
homem = 0
mulher = 0
totidade = 0
# Coleta dos dados
pesquisados = int(input('Quantas pessoas serão pesquisadas? '))

for i in range(0, pesquisados):
    #nome = str(input('Qual o seu nome? '))
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo? H ou M? '))
    totidade += idade
    if sexo == 'M' and idade < 20:
        mulher += 1
    if i == 1 and sexo == 'H':
        homem = idade
    else:
        if sexo == 'H' and homem < idade:
            homem = idade

print(f'A média de idade é de {totidade/pesquisados}')
print(f'A idade do homem mais velho é de {homem}.')
print(f'Existem {mulher} com menos de 20 anos.')
