import math

a = float(input('Qual o ângulo em graus você deseja calcular seno, cosseno e tangente? '))

b = math.radians(a)

sin = math.sin(b)
cos = math.cos(b)
tg = math.tan(b)

print(f'Então, para esse ângulo temos os seguintes valores: \n seno = {sin}; \n cosseno = {cos}; e \n tangente = {tg}.')