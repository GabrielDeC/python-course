p = float(input('Qual o preço do produto? '))
d = float(input('Qual o desconto da promoção? '))

print('O preço na promoção é R$ {:.2f}!'.format(float(p*(1-(d/100)))))
