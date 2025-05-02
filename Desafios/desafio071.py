saque = int()
div = int()
while True:
  saque = int(input('Qual o valor de saque? '))
  if saque >= 50:
    print(f'O saque será gerado em {saque // 50} notas de 50.')
    div = 50*(saque//50)
    saque = saque - div
  if saque >= 20 and saque < 50:
    print(f'O saque será gerado em {saque // 20} notas de 20.')
    div = 20*(saque//20)
    saque = saque - div
  if saque >= 10 and saque < 20:
    print(f'O saque será gerado em {saque // 10} notas de 10.')
    div = 10*(saque//10)
    saque = saque - div
  if saque >= 1 and saque < 10:
    print(f'O saque será gerado em {saque} notas de 1.')
    break