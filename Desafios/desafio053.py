frase = str(input('Insira uma frase para validar se é palíndromo: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
palindromo = ''
for i in range(len(junto) - 1, -1, -1):
    palindromo += junto[i]

if palindromo == junto:
    print('Essa palavra é palíndromo!')
else:
    print('Essa palavra não é palíndromo!')
