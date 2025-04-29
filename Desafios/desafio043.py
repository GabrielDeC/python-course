peso = float(input('Qual o seu peso? '))
altura = int(input('Qual sua altura em centímetros? '))

IMC = peso/((altura/100)**2)

if IMC < 18:
    print('Abaixo do Peso!')
elif IMC >= 18 and IMC < 25:
    print('Peso Ideal!')
elif IMC >= 25 and IMC < 30:
    print('Sobrepeso!')
elif IMC >= 30 and IMC < 40:
    print('Obesidade!')
elif IMC >= 40:
    print('Obesidade Mórbida!')