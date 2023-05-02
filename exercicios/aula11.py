import random

# 1. Escreva um loop for que imprima os números de 1 a 10.
for i in range(1, 11):
    print(i)

# 2. Escreva um loop while que imprima os números de 1 a 10.
i = 1
while i <= 10:
    print(i)
    i += 1

# 3. Escreva um loop for que imprima os números pares de 1 a 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 4. Escreva um loop while que imprima os números pares de 1 a 20.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 5. Escreva um loop for que imprima os números ímpares de 1 a 20.
for i in range(1, 21):
    if i % 2 == 1:
        print(i)

# 6. Escreva um loop while que imprima os números ímpares de 1 a 20.
i = 1
while i <= 20:
    if i % 2 == 1:
        print(i)
    i += 1

# 7. Escreva um loop for que calcule a soma dos números de 1 a 10.
soma = 0
for i in range(1, 11):
    soma += i
print(f'A soma é {soma}.')

# 8. Escreva um loop while que calcule a soma dos números de 1 a 10.
soma = 0
i = 1
while i <= 10:
    soma += i
    i += 1
print(f'A soma é {soma}.')

# 9. Escreva um loop for que calcule o produto dos números de 1 a 5.
produto = 1
for i in range(1, 6):
    produto *= i
print(f'O produto é {produto}.')

# 10.  Escreva um loop while que calcule o produto dos números de 1 a 5.
produto = 1
i = 1
while i <= 5:
    produto *= i
    i += 1
print(f'O produto é {produto}.')

# 11.  Escreva um loop for que imprima os caracteres de uma string.
for i in 'Python':
    print(i)

# 12.  Escreva um loop while que imprima os caracteres de uma string.
i = 0
while i < len('Python'):
    print('Python'[i])
    i += 1

# 13.  Escreva um loop for que encontre o maior elemento de uma lista.
lista = [1, 2, 3, 4, 5]
maior = lista[0]
for i in lista:
    if i > maior:
        maior = i
print(f'O maior elemento é {maior}.')

# 14.  Escreva um loop while que encontre o maior elemento de uma lista.
lista = [1, 2, 3, 4, 5]
maior = lista[0]
i = 0
while i < len(lista):
    if lista[i] > maior:
        maior = lista[i]
    i += 1
print(f'O maior elemento é {maior}.')

# 15.  Escreva um loop for que encontre o menor elemento de uma lista.
lista = [1, 2, 3, 4, 5]
menor = lista[0]
for i in lista:
    if i < menor:
        menor = i
print(f'O menor elemento é {menor}.')

# 16.  Escreva um loop while que encontre o menor elemento de uma lista.
lista = [1, 2, 3, 4, 5]
menor = lista[0]
i = 0
while i < len(lista):
    if lista[i] < menor:
        menor = lista[i]
    i += 1
print(f'O menor elemento é {menor}.')

# 17.  Escreva um loop for que conte o número de elementos em uma lista.
lista = [1, 2, 3, 4, 5]
contador = 0
for i in lista:
    contador += 1
print(f'A lista tem {contador} elementos.')

# 18.  Escreva um loop while que conte o número de elementos em uma lista.
lista = [1, 2, 3, 4, 5]
contador = 0
i = 0
while i < len(lista):
    contador += 1
    i += 1
print(f'A lista tem {contador} elementos.')

# 19.  Escreva um loop for que inverta uma string.
string = 'Python'
for i in range(len(string) - 1, -1, -1):
    print(string[i])

# 20.  Escreva um loop while que inverta uma string.
string = 'Python'
i = len(string) - 1
while i >= 0:
    print(string[i])
    i -= 1

# 21.  Escreva um loop for para criar uma lista de números de 1 a 50. Use um loop while interno para verificar se cada número é primo.
lista = []
for i in range(1, 51):
    # verificando se o número i é primo com o while
    primo = True
    j = 2
    while j < i:
        if i % j == 0:
            primo = False
        j += 1
    if primo:
        lista.append(i)
print(lista)

# 22.  Escreva um loop while que lê uma lista de números do usuário e depois use um loop for para iterar sobre a lista e calcular a soma dos valores.
lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break
    lista.append(numero)
soma = 0
for i in lista:
    soma += i
print(f'A soma é {soma}.')

# 23.  Escreva um loop for que imprime uma pirâmide de asteriscos de tamanho inserido pelo usuário. Use um loop while interno para controlar o número de asteriscos em cada linha.
tamanho = int(input('Digite o tamanho da pirâmide: '))
for i in range(1, tamanho + 1):
    # imprimindo os espaços
    for j in range(tamanho - i):
        print(' ', end='')
    # imprimindo os asteriscos, mas usando um while
    j = 0
    while j < i:
        print('*', end='')
        j += 1
    print()

# 24.  Escreva um loop while que encontre o segundo maior elemento de uma lista. Depois use um loop for para iterar sobre a lista e encontrar o segundo menor elemento.
# gerando uma lista aleatória com compreenção de lista
lista = [random.randint(1, 100) for i in range(20)]

# buscando o maior elemento
maior = lista[0]
i = 0
while i < len(lista):
    if lista[i] > maior:
        maior = lista[i]
    i += 1
# buscar o segundo maior elemento
segundo_maior = lista[0]
i = 0
while i < len(lista):
    if lista[i] > segundo_maior and lista[i] != maior:
        segundo_maior = lista[i]
    i += 1

# buscando o menor elemento
menor = lista[0]
i = 0
while i < len(lista):
    if lista[i] < menor:
        menor = lista[i]
    i += 1
# buscando o segundo menor elemento
segundo_menor = lista[0]
i = 0
while i < len(lista):
    if lista[i] < segundo_menor and lista[i] != menor:
        segundo_menor = lista[i]
    i += 1
# exibindo os resultados
print(f'A lista é {lista}.')
print(f'O segundo maior elemento é {segundo_maior}.')
print(f'O segundo menor elemento é {segundo_menor}.')

# 25.  Escreva um loop for que imprime as tabuadas de multiplicação de 1 a 10. Use um loop while interno para iterar sobre os números de 1 a 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')
    print()

# 26.  Escreva um loop while que lê uma lista de números do usuário e depois use um loop for para remover todos os valores duplicados. Depois, mostre uma lista contendo apenas os valores duplicados.
lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break
    lista.append(numero)
# removendo os valores duplicados
for i in lista:
    while lista.count(i) > 1:
        del lista[i]
print(lista)

# 27.  Escreva um loop for que calcula a soma dos quadrados dos números de 1 a 10 e salve em uma lista. Depois, use um loop while para iterar sobre a lista mostrando apenas os números pares.
lista = []
for i in range(1, 11):
    lista.append(i ** 2)
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        print(lista[i])
    i += 1

# 28.  Escreva um loop while que lê uma lista de nomes do usuário. Depois, use um for loop para verificar se um nome específico está na lista.
lista = []
while True:
    nome = input('Digite um nome: ')
    if nome == '':
        break
    lista.append(nome)
# usando um for loop para ver se um nome está na lista
for _ in lista:
    nome = input('Digite um nome para verificar se está na lista: ')
    if nome in lista:
        print(f'{nome} está na lista.')
    else:
        print(f'{nome} não está na lista.')
print('Todos os nomes foram verificados.')

# 29.  Escreva um loop while que lê uma lista de números do usuário. Depois use um loop for para iterar sobre a lista e calcular a soma dos valores.
lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break
    lista.append(numero)
soma = 0
for i in lista:
    soma += i
print(f'A soma é {soma}.')

# 30.  Escreva um loop for que imprime as tabuadas de adição de 1 a 10. Use um loop while interno para iterar sobre os números de 1 a 10.
for i in range(1, 11):
    j = 1
    while j < 11:
        print(f'{i} + {j} = {i + j}')
        j += 1
    print()

# 31.  Escreva um loop for que imprime as tabuadas de subtração de 1 a 10. Use um loop while interno para iterar sobre os números de 1 a 10.
for i in range(1, 11):
    j = 1
    while j < 11:
        print(f'{i} - {j} = {i - j}')
        j += 1
    print()

# 32.  Escreva um loop for que imprime as tabuadas de multiplicação de 1 a 10. Use um loop while interno para iterar sobre os números de 1 a 10.
for i in range(1, 11):
    j = 1
    while j < 11:
        print(f'{i} * {j} = {i * j}')
        j += 1
    print()

# 33.  Escreva um loop for que imprime as tabuadas de divisão de 1 a 10. Use um loop while interno para iterar sobre os números de 1 a 10.
for i in range(1, 11):
    j = 1
    while j < 11:
        print(f'{i} / {j} = {i / j}')
        j += 1
    print()

# 34.  Escreva um loop for que imprime as tabuadas de potenciação de 1 a 10. Use um loop while interno para iterar sobre os números de 1 a 10.
for i in range(1, 11):
    j = 1
    while j < 11:
        print(f'{i} ** {j} = {i ** j}')
        j += 1
    print()

# 35.  Escreva um loop for que imprime uma pirâmide de números. Use um loop while interno para mostrar cada linha com seu respectivo número.
altura = 9
for i in range(1, altura + 1):
    espacos = altura - i
    j = 1
    while j <= espacos:
        print(' ', end='')
        j += 1
    j = 1
    while j <= i:
        print(f'{i} ', end='')
        j += 1
    print()
