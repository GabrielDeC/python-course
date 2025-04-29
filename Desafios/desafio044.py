preco = float(input('Qual o valor a ser pago em R$? '))

print(f'Digite 1 para pagamento à vista: R$ {preco*0.9}\nDigite 2 para pagamento no cartão à vista: R$ {preco*0.95}\nDigite 3 para pagamento em 2x no cartão: R$ {preco}\nDigite 4 para pagamento em 3x ou mais no cartão: R$ {preco/0.8}')

condicao = int(input('Qual condição de pagamento você prefere? '))

if condicao == 1:
    print(f'O valor a ser pago será de R$ {preco*0.9}')
elif condicao == 2:
    print(f'O valor a ser pago será de R$ {preco*0.95}')
elif condicao == 3:
    print(f'O valor a ser pago será de R$ {preco}')
elif condicao == 4:
    print(f'O valor a ser pago será de R$ {preco/0.8}')