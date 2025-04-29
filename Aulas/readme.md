<h1>Estudos Iniciais de Python</h1>

<h2>Como uma linguagem funciona?</h2>

<p>
O código vai funcionar como um intérprete/interpretador da linguagem de máquina para um código na liguagem desejada.
A instalação no Linux pode ser reealizada direto pelo sudo apt get install python.
</p>

<h2>Primeiros Comandos</h2>

<p>
Todos os comando no Python são funções e para 'chamar' a função, é necessário fechar os parênteses, exemplo print() e sem a necessidade de ;
Os dados em Python em texto, sempre tem delimitadores que são as "" ou ''. Para números pode estar acompanhado de delimitadores.
Na função de print, os separados de concatenação de texto pode ser o + para concatenação sem espaços e se necessário espaço, pode ser colocado a , também para juntar tipos diferentes.
</p>

<h3>Variáveis</h3>

<p>
Todas as variáveis são escritas em minúscula e sempre lembrar que todas as variáveis no python são objetos.
A forma de atribuir o valor a uma variável é com igual, Exemplo:

nome = '' --> Definir dessa forma a variável fica "fixa"

para que seja pedido uma info dessa variável é utilizando o input('')

Em uma print, é possível colocar a variável no meio do texto a ser escrito por meio da seguinte função .format()
Ex.: 

nome = 'gabriel'
print('É um prazer te conhecer, {}'.format(nome))
</p>