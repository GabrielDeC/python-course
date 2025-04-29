km = int(input('Quantos Kms tem sua viagem? '))

if km <= 200:
    print(f'Sua passagem custará R$ {km*0.50}!')
else:
    print(f'Sua passagem custará R$ {km*0.45}!')