import random

# variáveis serão usadas ao longo dos exercícios
poema = """Três Anéis para os Reis-Elfos sob este céu;
Sete para os Senhores-Anões em seus rochosos corredores;
Nove para os Homens Mortais fadados a morrer;
Um para o Senhor do Escuro em seu Escuro Trono,
Na terra de Mordor, onde as Sombras se deitam.
Um Anel para a todos governar, Um Anel para encontrá-los,
Um Anel para a todos trazer e na Escuridão aprisioná-los,
Na terra de Mordor, onde as Sombras se deitam."""
lista = poema.split()

# 1. Crie uma lista de números inteiros e use um loop for para imprimir apenas os números pares.
numeros = [range(25)]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)

# 2. Crie uma lista de palavras e use um loop for para imprimir apenas as palavras que contêm a letra "a".
palavras = []
for i in range(25):
    palavras.append(random.choice(lista))

for palavra in palavras:
    if 'a' in palavra:
        print(palavra)

# 3. Crie uma variável inteira e use um comando if para verificar se ela é positiva ou negativa.
numero = random.randint(-100, 100)
if numero > 0:
    print('positivo')
else:
    print('negativo')

# 4. Crie uma variável float e use um comando if para verificar se ela é maior do que 10.
numero = random.uniform(-100.0, 100.0)
if numero > 10:
    print('maior que 10')
else:
    print('menor que 10')

# 5. Crie uma lista de números inteiros e use um loop for para encontrar o maior número da lista.
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))
print(numeros)

maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
print(maior)

# 6. Crie uma lista de strings e use um loop for para concatenar todas as strings em uma única string.
palavras = []
for i in range(25):
    palavras.append(random.choice(lista))
print(palavras)
junto = ''
for palavra in palavras:
    junto += palavra
print(junto)

# 7. Crie uma lista de booleanos e use um loop for para verificar se todos os valores são verdadeiros.
booleanos = []
for i in range(25):
    booleanos.append(random.choice([True, False]))
print(booleanos)
todos = True
for booleano in booleanos:
    if booleano == False:
        todos = False
print(todos)

# 8. Crie uma lista de números inteiros e use um loop for para calcular a média dos números.
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))
print(numeros)
soma = 0
for numero in numeros:
    soma += numero
media = soma / len(numeros)
print(media)

# 9. Crie uma lista de strings e use um loop for para contar quantas palavras têm mais de 5 caracteres.
palavras = []
for palavra in lista:
    if len(palavra) > 5:
        palavras.append(palavra)
print(palavras)

# 10. Crie uma variável booleana e use um comando if para verificar se ela é verdadeira ou falsa.
booleano = random.choice([True, False])
if booleano == True:
    print('verdadeiro')
else:
    print('falso')

# 11. Crie uma variável inteira e use um comando if para verificar se ela é divisível por 3.
numero = random.randint(0, 100)
if numero % 3 == 0:
    print('divisível por 3')
else:
    print('não divisível por 3')

# 12. Crie uma variável float e use um comando if para verificar se ela está entre 5.2 e 10.9.
numero = random.uniform(-100.0, 100.0)
if numero > 5.2 and numero < 10.9:
    print('entre 5.2 e 10.9')
else:
    print('não entre 5.2 e 10.9')

# 13. Crie uma lista de números inteiros e use um loop for para calcular a soma dos números.
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))
print(numeros)
soma = 0
for numero in numeros:
    soma += numero
print(soma)

# 14. Crie uma lista de strings e use um loop for para imprimir apenas as palavras que começam com a letra "a".
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    if planeta[0] == 'M':
        print(planeta)

# 15. Crie uma lista de booleanos e use um loop for para verificar se há pelo menos um valor verdadeiro na lista.
booleanos = []
for i in range(25):
    booleanos.append(random.choice([True, False]))
print(booleanos)
verdadeiro = False
for booleano in booleanos:
    if booleano == True:
        verdadeiro = True
print(verdadeiro)

# 16. Crie uma lista de números inteiros e use um loop for para imprimir apenas os números que são múltiplos de 5.
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))
print(numeros)
for numero in numeros:
    if numero % 5 == 0:
        print(numero)

# 17. Crie uma lista de strings e use um loop for para imprimir apenas as palavras que terminam com a letra "s".
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    if planeta[-1] == 'o':
        print(planeta)

# 18. Crie uma variável string e use um comando if para verificar se ela contém a palavra "python".
frase = 'python é uma linguagem de programação'
if 'python' in frase:
    print('contém python')

# 19. Crie uma variável booleana e use um comando if para verificar se ela é diferente de True.
booleano = random.choice([True, False])
if booleano != True:
    print('diferente de True')

# 20. Crie uma lista de números inteiros e use um loop for para encontrar o menor número da lista.
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))

menor = numeros[0]
for num in numeros:
    if num < menor:
        menor = num
print(menor)

# 21. Crie uma lista de listas, onde cada lista interna contém informações sobre uma pessoa, como nome, idade e profissão. Use um loop for para imprimir apenas os nomes das pessoas com mais de 30 anos.
pessoas = [
    ['João', 25, 'programador'],
    ['Maria', 30, 'professora'],
    ['José', 35, 'médico'],
    ['Ana', 40, 'advogada'],
]
for pessoa in pessoas:
    if pessoa[1] > 30:
        print(pessoa[0])

# 22. Crie uma lista de listas, onde cada lista contém informações sobre um produto, como nome, preço e quantidade em estoque. Use um loop for para imprimir apenas os produtos que estão em falta.
produtos = [
    ['camiseta', 50.0, 10],
    ['calça', 100.0, 0],
    ['bermuda', 80.0, 5],
]

for produto in produtos:
    if produto[2] == 0:
        print(produto[0])

# 23. Crie uma variável string que contém uma frase e use um loop for para imprimir, sem repetições. Exemplo: para a frase "o rato roeu a roupa do rei de Roma", a saída seria "o rateupdiRm".
frase = 'o rato roeu a roupa do rei de Roma'
letras = []
for letra in frase:
    if letra not in letras:
        letras.append(letra)
print(''.join(letras))

# 24. Crie um programa que receba dois números e gere uma lista de todos os números entre os dois passados. Exemplo: se o usuário digitar 1 e 6, deve gerar uma lista [2,3,4,5]. Se digitar 5 e 2, deve gerar uma lista [3,4]. Se digitar 3 e 3, vai gerar uma lista vazia.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
numeros = []
if num1 < num2:
    for i in range(num1 + 1, num2):
        numeros.append(i)
else:
    for i in range(num2 + 1, num1):
        numeros.append(i)
print(numeros)

# 25. Crie um programa que recebe uma lista de números inteiros e um número inteiro do usuário, e crie uma lista com todos os números da lista original que são maiores do que o número do usuário.
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))

num = int(input('Digite um número: '))
maiores = []
for numero in numeros:
    if numero > num:
        maiores.append(numero)
print(maiores)

# 26. Crie um programa que recebe uma lista de strings e um número inteiro do usuário, e cria uma lista com todas as strings da lista original que têm mais de n caracteres, onde n é o número digitado pelo usuário.
strings = ['python', 'java', 'c', 'c++', 'javascript', 'php', 'ruby', 'go', 'kotlin', 'swift']
num = int(input('Digite um número: '))

maiores = []
for string in strings:
    if len(string) > num:
        maiores.append(string)
print(maiores)

# 27. Crie um programa que recebe uma lista de números inteiros e um número inteiro do usuário, e crie uma lista com todos os números da lista original que são múltiplos do número passado do usuário.
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))

num = int(input('Digite um número: '))
multiplos = []
for numero in numeros:
    if numero % num == 0:
        multiplos.append(numero)
print(multiplos)

# 28. Crie uma lista de listas, onde cada lista contém informações sobre um filme, como título, diretor e ano de lançamento. Use um loop for e um comando if para imprimir apenas os títulos dos filmes lançados antes de 2000.
filmes = [
    ['O Poderoso Chefão', 'Francis Ford Coppola', 1972],
    ['O Poderoso Chefão II', 'Francis Ford Coppola', 1974],
    ['Batman', 'Tim Burton', 1989],
    ['Predador', 'John McTiernan', 1987],
    ['Alien, o Oitavo Passageiro', 'Ridley Scott', 1979]
]
for filme in filmes:
    if filme[2] < 1980:
        print(filme[0])

# 29. Crie uma lista de listas, onde cada lista contém informações sobre um livro, como título, autor e número de páginas. Use um loop for e um comando if para imprimir apenas os títulos dos livros que têm mais de 500 páginas.
livros = [
    ['O Poderoso Chefão', 'Mario Puzo', 448],
    ['O Senhor dos Anéis', 'J. R. R. Tolkien', 1200],
    ['Fundação', 'Isaac Asimov', 230],
    ['Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 223],
    ['O Hobbit', 'J. R. R. Tolkien', 300]
]
for livro in livros:
    if livro[2] > 500:
        print(livro[0])

# 30. Crie uma lista de strings e use um loop for e um comando if para imprimir apenas as strings que contêm apenas letras minúsculas.
strings = ['python', 'java', 'c', 'c++', 'javascript', 'php', 'ruby', 'go', 'kotlin', 'swift']
for string in strings:
    if string.islower():
        print(string)

# 31. Crie uma variável string e use um comando if para verificar se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente e de frente para trás).
palavra = 'arara'
if palavra == palavra[::-1]:
    print('É palíndromo')

# 32. Crie um programa que recebe uma lista de números inteiros e retorna a mediana da lista (ou seja, o número que fica no meio quando a lista é ordenada).
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))

numeros.sort()
if len(numeros) % 2 == 0:
    mediana = (numeros[len(numeros) // 2] + numeros[len(numeros) // 2 - 1]) / 2
else:
    mediana = numeros[len(numeros) // 2]
print(mediana)

# 33. Crie um programa que recebe uma lista de strings e retorna a string mais longa da lista.
linguagens = ['python', 'java', 'c', 'c++', 'javascript', 'php', 'ruby', 'go', 'kotlin', 'swift']
maior = linguagens[0]

for linguagem in linguagens:
    if len(linguagem) > len(maior):
        maior = linguagem
print(maior)

# 34. Crie um programa que recebe uma lista de números inteiros e mostre o número que aparece com mais frequência na lista.
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))

maior = numeros[0]
for numero in numeros:
    if numeros.count(numero) > numeros.count(maior):
        maior = numero
print(maior)

# 35. Crie uma lista de listas, onde cada lista contém informações sobre um funcionário, como nome, cargo e salário. Use um loop for e um comando if para imprimir apenas os nomes dos funcionários que ganham mais de R$ 5.000 por mês.
funcionarios = [
    ['João', 'Analista de Sistemas', 5000],
    ['Maria', 'Gerente de Projetos', 8000],
    ['José', 'Desenvolvedor', 6000],
    ['Ana', 'Analista de Sistemas', 5500],
    ['Pedro', 'Desenvolvedor', 7000]
]
for funcionario in funcionarios:
    if funcionario[2] > 5000:
        print(funcionario[0])

# 36. Crie uma lista de listas, onde cada lista contém informações sobre um aluno, como nome, idade e notas em matemática, português e ciências. Use um loop for e um comando if para imprimir apenas os nomes dos alunos que têm média maior do que 7 em todas as matérias.
alunos = [
    ['João', 15, 8, 7, 9],
    ['Maria', 16, 9, 8, 9],
    ['José', 15, 7, 6, 8],
    ['Ana', 16, 9, 9, 9],
    ['Pedro', 15, 8, 7, 8]
]

for aluno in alunos:
    media = (aluno[2] + aluno[3] + aluno[4]) / 3
    if media > 7:
        print(aluno[0])

# 37. Crie um programa que recebe uma lista de números inteiros e retorna uma nova lista com os números ordenados em ordem decrescente.
numeros = []
for i in range(25):
    numeros.append(random.randint(0, 100))

# bubble sort reverso
for i in range(len(numeros)):
    for j in range(len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print(numeros)

# 38. Crie um programa que recebe uma lista de strings e retorna uma nova lista com as strings ordenadas em ordem alfabética inversa.
linguagens = ['python', 'java', 'c', 'c++', 'javascript', 'php', 'ruby', 'go', 'kotlin', 'swift']

for linguagem in linguagens:
    for i in range(len(linguagens)):
        for j in range(len(linguagens)):
            if linguagens[i] > linguagens[j]:
                linguagens[i], linguagens[j] = linguagens[j], linguagens[i]
print(linguagens)

# 39. Crie uma lista de listas, onde cada lista contém informações sobre um carro, como marca, modelo e ano de fabricação. Use um loop for e um comando if para imprimir apenas as marcas dos carros que foram fabricados antes de 2010.
carros = [
    ['Fiat', 'Uno', 2000],
    ['Ford', 'Ka', 2015],
    ['Chevrolet', 'Onix', 2018],
    ['Volkswagen', 'Gol', 2010],
    ['Fiat', 'Palio', 2005]
]

for carro in carros:
    if carro[2] < 2010:
        print(carro[0])

# 40. Crie uma lista de listas, onde cada lista contém informações sobre um produto, como nome, preço e peso. Use um loop for e um comando if para imprimir apenas os nomes dos produtos que têm preço maior do que R$ 100 e peso menor do que 1 kg.
produtos = [
    ['Notebook', 3000, 2],
    ['Smartphone', 2000, 0.5],
    ['Tablet', 1500, 1],
    ['Smartwatch', 500, 0.2],
    ['Smart TV', 3000, 5]
]

for produto in produtos:
    if produto[1] > 100 and produto[2] < 1:
        print(produto[0])
