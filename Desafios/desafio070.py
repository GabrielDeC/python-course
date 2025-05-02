produto_nome = str()
produto_preco = float()
total = float()
contagem = int()
produtos_barato = float()
produtos_maior_1000 = float()

while True:
  produto_nome = str(input('Qual produto será registrado para compra? ')).strip()
  produto_preco = float(input('Qual o preço do produto? '))
  total += produto_preco
  if produto_preco >= 1000.00:
    produtos_maior_1000 += 1
  if contagem == 0:
    produtos_barato = produto_preco
  else:
    if produtos_barato > produto_preco:
      produtos_barato = produto_preco
  contagem += 1
  add_produto = str(input('Deseja adicionar mais algum produto? [S ou N] ')).upper().strip()
  if add_produto == "N":
    break

print(f'O total de gastos foi de R$ {total}, os produtos acima de R$ 1.000,00 foi de {produtos_maior_1000} e o produto mais barato foi de R$ {produtos_barato}')