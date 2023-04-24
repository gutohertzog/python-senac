"""exercícios realizados da Aula 01"""
# 01.	Qual o caractere de escape utilizado para quebrar linha em uma string?
print('O caractere de escape usado \npara quebrar a linha é o barra n ("\\n")')

# 02.	Escreva uma string que utilize o caractere de escape para imprimir uma citação entre aspas 
# duplas e o nome do autor.
citacao = '"Um mago nunca se atrasa", Gandalf'
print(citacao)

# 03.	Qual é o resultado da expressão: 10 + 5 / 2 * 3 - 1
print('10 + 5 / 2 * 3 - 1 =', 10 + 5 / 2 * 3 - 1)

# 04.	Como usar a função type para descobrir o tipo de dado de uma variável?
print('Coloca a variável dentro da função, type(15) =', type(15))

# 05.	Qual o resultado da expressão: 10 / 5 + 3 * 2 - 1
print('10 / 5 + 3 * 2 - 1 =', 10 / 5 + 3 * 2 - 1)

# 06.	Como utilizar o método format para inserir variáveis em uma string?
print('usa-se chamando ele ao final da string. exemplo: "o valor x é {}".format(x)')

# 07.	Qual o resultado da expressão: 5 ** 2
print('5 ** 2 =', 5 ** 2)

# 08.	Qual o resultado da expressão: 10 % 3
print('10 % 3 =', 10 % 3)

# 09.	Escreva uma string que utilize o caractere de escape para imprimir uma barra invertida.
print('barra invertida \\')

# 10.	Qual o resultado da expressão: 10 // 3
print('10 // 3 =', 10 // 3)

# 11.	Escreva uma string que utilize o método format para imprimir o nome e a idade de uma pessoa.
nome = 'Tom Cruise'
idade = 60
print('O nome é {c1} e tem {c2} anos.'.format(c1=nome, c2=idade))

# 12.	Qual o resultado da expressão: 15 - 7 * (8 / 4 + 2)
print('15 - 7 * (8 / 4 + 2) =', 15 - 7 * (8 / 4 + 2))

# 13.	Escreva uma string que utilize o método format para imprimir o valor de uma variável inteira.
x = 42
print('O valor de x é {valor}.'.format(valor=x))

# 14.	Qual o resultado da expressão: 2 + 3 * 4
print('2 + 3 * 4 =', 2 + 3 * 4)

# 15.	Escreva uma string que utilize o caractere de escape para imprimir uma tabulação.
print('uma \t tabulação')

# 16.	Qual o resultado da expressão: 2 ** 3 + 4
print('2 ** 3 + 4 =', 2 ** 3 + 4)

# 17.	Escreva uma string que utilize o método format para imprimir o valor de uma variável float com duas casas decimais.
pi = 3.1415
print('O valor de pi é {:.2f}.'.format(pi))

# 18.	Crie uma string que mostre seu ano de nascimento com base na idade atual.
idade = 60
print('Tam Cruise nasceu no ano de {res}.'.format(res=2023 - idade))

# 19.	Qual o resultado da expressão: (2 + 3) * 4
print('(2 + 3) * 4 =', (2 + 3) * 4)

# 20.	Escreva uma string que utilize o caractere de escape para imprimir um caractere de aspa simples.
print('\'estou entre aspas simples\'')

# 21.	Qual o resultado da expressão: 10 / (2 + 3) * 4
print('10 / (2 + 3) * 4 =', 10 / (2 + 3) * 4)

# 22.	Crie uma variável que armazene um texto com seu nome completo, concatene com uma mensagem de saudação e a imprima.
saudacao = 'Bem-vindo, '
nome = 'Tom Cruise'
completo = saudacao + nome  # concatena e salva em uma nova variável
print(completo)

# 23.	Crie uma string que utilize o método format para inserir o seu nome em uma mensagem.
nome = 'Tom Cruise'
print('{0}'.format(nome))

# 24.	Crie uma string que utilize o método format para inserir a sua idade em uma mensagem.
idade = 60
print('{0}'.format(idade))

# 25.	Crie uma string que utilize o método format para inserir um número decimal em uma mensagem.
decimal = '3.14'
print('{0}'.format(decimal))

# 26.	Crie uma string que utilize o método format para inserir um número inteiro em uma mensagem.
inteiro = '42'
print('{0}'.format(inteiro))

# 27.	Crie uma string que utilize o método format para inserir duas strings em uma mensagem.
nome = 'Tom Cruise'
idade = '60'
texto = 'O {1} tem {0} anos.'.format(idade, nome)
print(texto)

# 28.	Crie uma string que utilize o método format para inserir três números inteiros em uma mensagem.
texto = '{0} + {2} = {1}'.format(1, 1 + 2, 2)
print(texto)

# 29.	Crie uma string que utilize o método format para inserir duas strings e um número inteiro em uma mensagem.
mensagem = '{} {} {} anos'.format('Tom Cruise', 'tem', 60)
print(mensagem)

# 30.	Crie uma string que utilize o método format para inserir uma string e um número decimal em uma mensagem.
texto = '{0} {1}'.format('pi', 3.1415)
print(texto)

# 31.	Crie uma string que utilize o método format para inserir dois números inteiros e um número decimal em uma mensagem.
texto = 'número : {}  resposta : {}  pi : {}'.format(5, 42, 3.14)
print(texto)

# 32.	Crie uma string que utilize o método format para inserir três números decimais em uma mensagem.
texto = 'três floats : {} {} {}'.format(3.14, 5.2, 4.2)
print(texto)

# 33.	Crie uma string que utilize o método format para inserir uma string e dois números decimais em uma mensagem.
texto = '{nome} {idade} {peso}'.format(
    nome='Tom Cruise', idade=1.70, peso=67.8)
print(texto)

# 34.	Crie uma string que utilize o método format para inserir três strings em uma mensagem.
texto = '{} {} {}'.format('Tom', 'Cruise', 'lindo!')
print(texto)

# 35.	Crie uma string que utilize o método format para inserir um número inteiro e duas strings em uma mensagem.
texto = '{} {} {}'.format(42, 'é a', 'resposta')
print(texto)

# 36.	Crie uma string que utilize o método format para inserir duas strings e um número decimal em uma mensagem.
texto = '{} {} tem {} de altura'.format('Tom', 'Cruise', 1.70)
print(texto)

# 37.	Crie uma string que utilize o método format para inserir três números float em uma mensagem, cada um com um número de casas decimais diferente.
texto = '{v1:.2f} {v3:.3f} {v2:.4f}'.format(v1=2.22222, v2=1.11111, v3=5.55555)
print(texto)

# 38.	Crie uma string que utilize o método format para inserir uma string e um número inteiro em uma mensagem, onde o número inteiro é apresentado em formato de porcentagem.
texto = '{nome} {perc}%'.format(nome='Tom', perc=40/100)
print(texto)

# 39.	Crie uma string que utilize o método format para inserir um número decimal em uma mensagem, onde o número é apresentado em notação científica.
valor = 254136410000.00000
texto = 'Valor científico de {} é {:e}'.format(valor, valor)
print(texto)

# 40.	Crie uma string que utilize o método format para inserir uma string e dois números inteiros em uma mensagem, onde os números inteiros são apresentados em formato de data.
texto = '{} : {}/{}'.format('a data é', 16, 4)
print(texto)

# 41.	Crie uma string que utilize o método format para inserir um número decimal em uma mensagem, onde o número é apresentado com um símbolo de moeda.
texto = 'R$ {}'.format(1.99)
print(texto)

# 42.	Crie uma string que utilize o método format para inserir uma string e um número decimal em uma mensagem, onde o número é apresentado com um número fixo de casas decimais.
texto = 'O nome é {} e tem {:.3} kg'.format('Tom', 75.5555555)
print(texto)

# 43.	Crie uma variável com um valor float e imprima uma string que informe o valor com duas casas decimais.
pi = 3.1415
print('pi 2 com duas casas decimais : {:.2f}'.format(pi))

# 44.	Crie uma variável que armazene um texto com um número no meio e transforme esse número em seu dobro.
num = 42
texto = 'o valor dobrado {} fica lindo'.format(42 * 2)
print(texto)

# 45.	Crie uma variável com um texto contendo uma palavra repetida três vezes.
texto = 'repetido-' * 3
print(texto)

# 46.	Crie 3 variáveis com as notas de três provas e mostre uma mensagem com a média do aluno.
nota1 = 5.0
nota2 = 6.9
nota3 = 7.9
media = (nota1 + nota2 + nota3) / 3
print('a média é : {:.2f}'.format(media))

# 47.	Crie uma string que contenha a palavra "olá" repetida 5 vezes utilizando o operador *.
palavra = 'olá'
print(palavra * 5)

# 48.	Crie uma string que contenha a palavra "mundo" repetida 3 vezes utilizando o operador *.
palavra = 'mundo'
print(palavra * 3)

# 49.	Crie uma string que contenha a palavra "Python" repetida 2 vezes e a palavra "é legal" uma vez utilizando o operador +.
texto = ('Python' * 2) + ' é legal'
print(texto)

# 50.	Crie uma string que contenha a palavra "programação" repetida 3 vezes utilizando o operador * e depois adicione " em Python" utilizando o operador +.
texto = 'programação' * 3
texto = texto + ' em Python'
print(texto)

# 51.	Crie uma string que contenha a palavra "amor" repetida 4 vezes utilizando o operador * e adicione " verdadeiro" no final utilizando o operador +.
texto = 'amor' * 4
texto += 'verdadeiro'
print(texto)

# 52.	Crie uma string que contenha a palavra "fácil" repetida 2 vezes, a palavra "Python" uma vez e a palavra "é" uma vez utilizando o operador +.
texto = 'fácil' * 2
texto += 'Python' + 'é'
print(texto)

# 53.	Crie uma string que contenha a palavra "casa" repetida 2 vezes utilizando o operador * e depois adicione " de praia" utilizando o operador +.
texto = 'casa' * 2
texto += ' de praia'
print(texto)

# 54.	Crie uma string que contenha a palavra "caminhar" repetida 3 vezes utilizando o operador * e adicione " na natureza" no final utilizando o operador +.
texto = 'caminhar' * 3
texto += ' na natureza'
print(texto)

# 55.	Crie uma string que contenha a palavra "trabalho" repetida 4 vezes utilizando o operador * e depois adicione " duro" utilizando o operador +.
texto = 'trabalho' * 4
texto += ' duro'
print(texto)

# 56.	Crie uma string que contenha a palavra "festa" repetida 2 vezes utilizando o operador * e adicione " de aniversário" utilizando o operador +.
texto = 'festa' * 2
texto = texto + ' de aniversário'
print(texto)

# 57.	Crie uma string que contenha a palavra "piscina" repetida 3 vezes utilizando o operador * e depois adicione " em casa" utilizando o operador +.
texto = 'piscina' * 3
texto += ' em casa'
print(texto)

# 58.	Crie uma string que contenha a palavra "frio" repetida 4 vezes utilizando o operador * e adicione " na montanha" no final utilizando o operador +.
print('frio' * 4, ' na montanha')

# 59.	Crie uma string que contenha a palavra "comida" repetida 2 vezes, a palavra "gostosa" uma vez e a palavra "é" uma vez utilizando o operador +.
texto = 'comida' * 2
texto += ' gostosa'
print(texto)

# 60.	Crie uma string que contenha a palavra "férias" repetida 3 vezes utilizando o operador * e depois adicione " na praia" utilizando o operador +.
texto = 'férias' * 3
texto += ' na praia'
print(texto)

# 61.	Crie uma string que contenha a palavra "estudar" repetida 4 vezes utilizando o operador * e adicione " é importante" utilizando o operador +.
texto = 'estudar ' * 4
texto += ' é importante'
print(texto)

# 62.	Crie uma string que contenha a palavra "livro" repetida 2 vezes utilizando o operador * e depois adicione " de aventura" utilizando o operador +.
texto = 'livro' * 2
texto += ' de aventura'
print(texto)

# 63.	Crie uma string que contenha a palavra "esporte" repetida 3 vezes utilizando o operador * e adicione " faz bem à saúde" no final utilizando o operador +.
texto = 'esporte ' * 3
texto += ' faz bem à saúde'
print(texto)

# 64.	Crie uma string que contenha a palavra "passear" repetida 4 vezes utilizando o operador * e depois adicione " no parque" utilizando o operador +.
texto = 'passear ' * 4
texto += ' no parte'
print(texto)

# 65.	Crie uma string que contenha a palavra "bebida" repetida 2 vezes, a palavra "gelada" uma vez e a palavra "é" uma vez utilizando o operador +.
texto = 'bebida ' * 2
texto += ' gelada'
texto += ' é'
print(texto)

# 66.	Crie uma string que contenha a palavra "música" repetida 3 vezes utilizando o operador * e adicione " alegra o dia" no final utilizando o operador +.
texto = 'musica ' * 3
texto += ' alegra o dia'
print(texto)

# 67.	Crie uma string onde mostre sua idade, seu nome e sua data de nascimento.
nome = 'Tom Cruise'
idade = 60
data_nasc = '03/07/1962'
print('O {} tem {} anos e nasceu em {}'.format(nome, idade, data_nasc))

