idade = maior = homens = mulheres20 = 0
sexo = str()
while True:
    idade = int(input('Qual a idade da pessoa? '))
    while True:
        sexo = str(input('Qual o seu sexo (M ou F)? ')).upper().strip()
        if sexo == "M" or sexo == "F":
            break
    if idade >= 18:
        maior += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade >= 20:
        mulheres20 += 1
    while True:
        registro = str(input('Deseja continuar o registro [S ou N]? ')).upper().strip()
        if registro == "S" or registro == "N":
            break
    if registro == 'N':
        break
print(f'Segue os dados coletados:\n[1] A quantidade de pessoas maiores de 18 anos: {maior}\n[2] A quantidade de homens cadastrados são de: {homens}\n[3] A quantidade de mulheres maiores de 20 anos é de: {mulheres20}\n\nAgradecemos pelo cadastro, volte sempre!')
