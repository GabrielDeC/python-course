n = soma = contagem = int()

while True:
    n = int(input('Qual número deseja adicionar para a soma? [999 para Sair]'))
    if n == 999:
        break
    soma += n
    contagem += 1

print(f'A soma dos números digitados é {soma} e foram {contagem} números digitados.')