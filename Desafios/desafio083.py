expressao = ''
parenteseEsquerdo = 0
parenteseDireito = 0
expressao = str(input('Digite uma expressão matemática com parênteses:\n'))
parenteseEsquerdo = expressao.count('(')
parenteseDireito = expressao.count(')')

if parenteseDireito == parenteseEsquerdo:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')