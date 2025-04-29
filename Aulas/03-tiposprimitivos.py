#Tipos primitivos

#São considerados as definições do que um dado é, por exemplo, int para inteiros, float para números decimais, bool para dados booleanos (V ou F) e str para string/texto.
# int() --> 1 / 2 / 3 ou qualquer inteiro
# float() --> 1.5 / 7.0 / 3.123 ou qualquer número real
# bool() --> True ou False
# str() --> 'texto qualquer' / '7.0' ou qualquer texto

# Toda informação dentro do input() se torna string.
# Se eu quero saber o tipo de uma variável type().

# .isnumeric() --> Função para saber se uma variável é numérica
# .isalpha() --> Função para saber se uma variável é Alfabético
# .isalphanum() --> Função para saber se uma variável é Alfanumérico
# .is...() --> Função para saber se uma variável se classifica em algum tipo de classe

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

soma = a + b

print('A soma vale {}'.format(soma))
