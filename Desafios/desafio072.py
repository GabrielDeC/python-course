extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
  escolha = int(input('Digite um número de 0 a 20 para mostrá-lo por extenso: '))
  if escolha >= 0 and escolha <= 20:
    print(extenso[escolha])
    break
  else:
    print(f'{escolha} não está entre 0 e 20. Por gentileza, digite novamente.')