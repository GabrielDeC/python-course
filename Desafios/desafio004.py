a = input('Digite qualquer tecla: ')

print("O dígito é numérico? {}".format(a.isnumeric()))
print("O dígito é alfabético? {}".format(a.isalpha()))
print("O dígito é alfanumérico? {}".format(a.isalnum()))
print("O dígito é tudo maiúsculo? {}".format(a.isupper()))
print("O dígito é tudo minúsculo? {}".format(a.islower()))
print("O dígito inserido é uma {}".format(type(a)))
