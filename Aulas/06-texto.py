# O texto em PY são arrays de strings que começam do 0 até o final.

# Como fatiar uma string? Utilizando a lista, Exemplo frase[9] vai puxar a string na posição 9 do array de frase ou frase[9:13] vai puxar as posições de 9 a 12 
# ou frase[9:21:2] vai mostrar as posições de 9 a 20 pulando sempre de 2 em 2 ou frase[:5] começa do 0 até o 4 ou frase[15:] vai do 15 até o final
# ou frase[9::3] significa que vai começar do 9 até o final pulando de 3 em 3.

# len(frase) --> encontra a quantidade de caracteres ou tamanho da frase.
# frase.count('') --> Serve para contar quantas vezes aparece a letra ou conjunto de caracteres entre '' e se estiver frase.count('', <int>, <int>) define a contagem já com fatiamento.
# frase.find('') --> Serve para procurar o início da primeira sequência dos caracteres entre ''.
# '' in frase --> Função boolena para informar se existe os caracteres na '' em frase.
# frase.replace('', '') --> Procura a primeira sequência de caracteres e substitui pela segunda.
# frase.upper(), frase.lower(), frase.capitalize() --> Muda de minúscula para maiúscula e vice-versa, coloca tudo em minúscula e apenas o primeir caractere em miúsculo.
# frase.title() --> Coloca todas as primeira letras de cada palavra em maiúsculo.
# frase.strip(), frase.rstrip(), frase.lstrip() --> Remove espaços adicionais aos lados da string, remove na direita, remove na esquerda.
# frase.split() --> Separa o array por todas as posições vazias ('espaços')
# ''.join(frase) --> Junta elementos em um único pelo separador inserido entre ''.
