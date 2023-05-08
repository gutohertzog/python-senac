# for e strings
# 1. Crie um programa que exiba cada caractere de uma string utilizando o laço de repetição for.
palavra = 'pneumoencefalografia'
for letra in palavra:
    print(letra)

# 2. Faça um programa que leia uma string e conte o seu tamanho utilizando o laço de repetição for (não utilize a função len).
palavra = input('Digite qualquer coisa : ')
contador = 0
for letra in palavra:
    contador += 1

# 3. Crie um programa que leia uma frase longa e exiba cada palavra em uma linha utilizando o laço de repetição for.
frase = input('Digite uma frase : ')
palavras = frase.split()
for palavra in palavras:
    print(palavra)

# 4. Faça um programa que leia uma string e exiba apenas as vogais utilizando o laço de repetição for.
palavra = input('Digite qualquer coisa : ')
for letra in palavra:
    if letra in 'aeiou':
        print(letra)

# 5. Crie um programa que leia uma string e exiba apenas as consoantes utilizando o laço de repetição for.
palavra = input('Digite qualquer coisa : ')
for letra in palavra:
    if letra not in 'aeiou':
        print(letra)

# 6. Faça um programa que leia uma string e exiba apenas as letras maiúsculas utilizando o laço de repetição for.
palavra = input('Digite qualquer coisa : ')
for letra in palavra:
    if letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(letra)

# 7. Crie um programa que leia uma string e exiba apenas as letras minúsculas utilizando o laço de repetição for.
palavra = input('Digite qualquer coisa : ')
for letra in palavra:
    if letra in 'abcdefghijklmnopqrstuvwxyz':
        print(letra)

# 8. Faça um programa que leia uma string e exiba cada caractere em uma linha utilizando o laço de repetição for.
palavra = input('Digite qualquer coisa : ')
for letra in palavra:
    print(letra)

# 9. Crie um programa que leia uma string e substitua todas as letras "a" por "*" utilizando o laço de repetição for (não utilize o método replace das strings).
palavra = input('Digite qualquer coisa : ')
formatada = ''
for letra in palavra:
    if letra.lower() == 'a':
        formatada += '*'
    else:
        formatada += letra
print(formatada)

# 10. Faça um programa que leia uma string e exiba a string invertida utilizando o laço de repetição for (não utilize listas para isso).
palavra = input('Digite qualquer coisa : ')
invertida = ''
for letra in palavra:
    invertida = letra + invertida
print(invertida)

# 11. Crie um programa que leia uma frase e exiba apenas as palavras que começam com a letra "a" utilizando o laço de repetição for. Se não tiver nenhuma palavra que comece com 'a', avise ao usuário.
frase = input('Digite uma frase : ')
palavras = frase.split()
achou = False
for palavra in palavras:
    if palavra[0].lower() == 'a':
        print(palavra)
        achou = True
if not achou:
    print('Não tem nenhuma palavra que comece com a letra "a".')

# 12. Faça um programa que leia uma string e verifique se ela é um palíndromo utilizando o laço de repetição for.
palavra = input('Digite qualquer coisa : ')
invertida = ''
for letra in palavra:
    invertida = letra + invertida
if palavra == invertida:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')

# 13. Crie um programa que leia uma string e exiba apenas as palavras que possuem mais de 5 caracteres utilizando o laço de repetição for.
frase = input('Digite uma frase : ')
palavras = frase.split()
for palavra in palavras:
    if len(palavra) > 5:
        print(palavra)

# 14. Faça um programa que leia uma frase e exiba apenas as palavras que possuem a letra "e" utilizando o laço de repetição for.
frase = input('Digite uma frase : ')
palavras = frase.split()
for palavra in palavras:
    if 'e' in palavra:
        print(palavra)

# 15. Crie um programa que leia uma string e conte quantas vezes uma determinada letra aparece na string utilizando o laço de repetição for (não utilize o método count das strings).
palavra = input('Digite qualquer coisa : ')
letra = input('Digite uma letra : ')
contador = 0
for l in palavra:
    if l == letra:
        contador += 1
print(f'A letra "{letra}" aparece {contador} vezes na palavra "{palavra}".')

# 16. Faça um programa que leia uma string e exiba apenas as palavras que terminam com a letra "o" utilizando o laço de repetição for.
frase = input('Digite uma frase : ')
palavras = frase.split()
for palavra in palavras:
    if palavra[-1].lower() == 'o':
        print(palavra)

# 17. Crie um programa que leia uma string e exiba apenas as palavras que possuem a letra "u" em qualquer posição utilizando o laço de repetição for.
frase = input('Digite uma frase : ')
palavras = frase.split()
for palavra in palavras:
    if 'u' in palavra:
        print(palavra)

# 18. Faça um programa que leia uma string e substitua todas as letras minúsculas por maiúsculas utilizando o laço de repetição for.
palavra = input('Digite qualquer coisa : ')
formatada = ''
for letra in palavra:
    if letra in 'abcdefghijklmnopqrstuvwxyz':
        formatada += letra.upper()
    else:
        formatada += letra

# 19. Crie um programa que leia uma string e exiba apenas as palavras que possuem a letra "i" em qualquer posição utilizando o laço de repetição for.
frase = input('Digite uma frase : ')
palavras = frase.split()
for palavra in palavras:
    if 'i' in palavra:
        print(palavra)

# 20. Crie um programa que leia uma lista de nomes e exiba-os na tela utilizando o laço de repetição for.
nomes = []
for i in range(5):
    nomes.append(input('Digite um nome : '))
for nome in nomes:
    print(nome)


# for e números
# 1. Crie um programa que exiba os números de 0 a 10 utilizando o laço de repetição for.
for i in range(11):
    print(i)

# 2. Faça um programa que exiba os números ímpares de 1 a 20 utilizando o laço de repetição for.
for i in range(1, 21, 2):
    print(i)

# 3. Crie um programa que exiba os números pares entre 0 e 50 utilizando o laço de repetição for.
for i in range(0, 51, 2):
    print(i)

# 4. Faça um programa que leia um número e exiba a tabuada de multiplicação desse número utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
for i in range(11):
    print(f'{numero} x {i} = {numero * i}')

# 5. Crie um programa que leia um número e exiba todos os números pares de 0 até esse número utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
for i in range(0, numero + 1, 2):
    print(i)

# 6. Faça um programa que leia um número e exiba todos os números ímpares de 0 até esse número utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
for i in range(1, numero + 1, 2):
    print(i)

# 7. Crie um programa que leia um número e exiba a soma de todos os números pares de 0 até esse número utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
soma = 0
for i in range(0, numero + 1, 2):
    soma += i

# 8. Faça um programa que leia um número e exiba a soma de todos os números ímpares de 0 até esse número utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
soma = 0
for i in range(1, numero + 1, 2):
    soma += i

# 9. Crie um programa que leia um número e exiba se ele é primo ou não utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
if primo:
    print('É primo')
else:
    print('Não é primo')

# 10. Crie um programa que leia um número e exiba todos os números primos de 0 até esse número utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
for i in range(2, numero + 1):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
    if primo:
        print(i)

# 11. Crie um programa que leia um número e exiba todos os números divisíveis por 3 de 0 até esse número utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
for i in range(0, numero + 1, 3):
    print(i)

# 12. Crie um programa que leia um número e exiba a sequência de Fibonacci até esse número utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
a = 0
b = 1
for i in range(numero):
    print(a)
    c = a + b
    a = b
    b = c

# 13. Faça um programa que leia um número e uma string e exiba a string a quantidade de vezes do número utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
palavra = input('Digite uma palavra : ')
for i in range(numero):
    print(palavra)

# 14. Crie um programa que leia um número e exiba a sua tabuada de adição utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
for i in range(11):
    print(f'{numero} + {i} = {numero + i}')

# 15. Faça um programa que leia um número e exiba a sua tabuada de subtração utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
for i in range(11):
    print(f'{numero} - {i} = {numero - i}')

# 16. Crie um programa que leia um número e exiba a sua tabuada de multiplicação utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
for i in range(11):
    print(f'{numero} * {i} = {numero * i}')

# 17. Faça um programa que leia um número e exiba a sua tabuada de divisão utilizando o laço de repetição for.
numero = int(input('Digite um número : '))
for i in range(11):
    print(f'{numero} / {i} = {numero / i}')

# 18. Crie um programa que leia um número e exiba o seu fatorial utilizando o laço de repetição for (não utilize a função factorial do módulo math).
numero = int(input('Digite um número : '))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(fatorial)

# for e listas
# 1. Faça um programa que leia uma lista de 10 números e calcule a média aritmética utilizando o laço de repetição for.
qtd = 10
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
soma = 0
for i in range(qtd):
    soma += numeros[i]
media = soma / qtd
print(media)

# 2. Faça um programa que leia uma lista de números e calcule o seu produto utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
produto = 1
for i in range(qtd):
    produto *= numeros[i]
print(produto)

# 3. Crie um programa que leia uma lista de nomes e exiba o número de caracteres de cada nome utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de nomes : '))
nomes = []
for i in range(qtd):
    nome = input('Digite um nome : ')
    nomes.append(nome)
for i in range(qtd):
    print(len(nomes[i]))

# 4. Faça um programa que leia uma lista de números e exiba o maior e o menor valor utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
maior = numeros[0]
menor = numeros[0]
for i in range(qtd):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
print('Maior : {}'.format(maior))
print('Menor : {}'.format(menor))

# 5. Faça um programa que leia uma lista de números e exiba apenas os números maiores que 10 utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
for i in range(qtd):
    if numeros[i] > 10:
        print(numeros[i])

# 6. Crie um programa que leia uma lista de nomes e exiba apenas os nomes que começam com a letra "A" utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de nomes : '))
nomes = []
for i in range(qtd):
    nome = input('Digite um nome : ')
    nomes.append(nome)
for i in range(qtd):
    if nomes[i][0] == 'A':
        print(nomes[i])

# 7. Faça um programa que leia uma lista de números e exiba apenas os números pares utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
for i in range(qtd):
    if numeros[i] % 2 == 0:
        print(numeros[i])

# 8. Crie um programa que leia uma lista de nomes e exiba apenas os nomes que contém a letra "e" utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de nomes : '))
nomes = []
for i in range(qtd):
    nome = input('Digite um nome : ')
    nomes.append(nome)
for i in range(qtd):
    if 'e' in nomes[i]:
        print(nomes[i])

# 9. Faça um programa que leia uma lista de números e exiba a soma dos números pares utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
soma = 0
for i in range(qtd):
    if numeros[i] % 2 == 0:
        soma += numeros[i]
print(soma)

# 10. Crie um programa que leia uma lista de nomes e exiba apenas os nomes que possuem mais de 5 caracteres utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de nomes : '))
nomes = []
for i in range(qtd):
    nome = input('Digite um nome : ')
    nomes.append(nome)
for i in range(qtd):
    if len(nomes[i]) > 5:
        print(nomes[i])

# 11. Faça um programa que leia uma lista de números e exiba a média aritmética dos números pares utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
soma = 0
qtd_pares = 0
for i in range(qtd):
    if numeros[i] % 2 == 0:
        soma += numeros[i]
        qtd_pares += 1
media = soma / qtd_pares
print(media)

# 12. Faça um programa que leia uma lista de números e exiba a média aritmética dos números ímpares utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
soma = 0
qtd_impares = 0
for i in range(qtd):
    if numeros[i] % 2 != 0:
        soma += numeros[i]
        qtd_impares += 1
media = soma / qtd_impares
print(media)

# 13. Crie um programa que leia uma lista de nomes e exiba apenas os nomes que possuem a letra "a" na segunda posição utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de nomes : '))
nomes = []
for i in range(qtd):
    nome = input('Digite um nome : ')
    nomes.append(nome)
for i in range(qtd):
    if nomes[i][1] == 'a':
        print(nomes[i])

# 14. Faça um programa que leia uma lista de números e exiba a soma dos números ímpares utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
soma = 0
for i in range(qtd):
    if numeros[i] % 2 != 0:
        soma += numeros[i]
print(soma)

# 15. Crie um programa que leia uma lista de nomes e exiba apenas os nomes que terminam com a letra "o" utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de nomes : '))
nomes = []
for i in range(qtd):
    nome = input('Digite um nome : ')
    nomes.append(nome)
for i in range(qtd):
    if nomes[i][-1] == 'o':
        print(nomes[i])

# 16. Crie um programa que leia uma lista de nomes e exiba apenas os nomes que possuem mais de uma vogal utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de nomes : '))
nomes = []
for i in range(qtd):
    nome = input('Digite um nome : ')
    nomes.append(nome)
for i in range(qtd):
    vogais = 0
    for j in range(len(nomes[i])):
        if nomes[i][j] in 'aeiou':
            vogais += 1
    if vogais > 1:
        print(nomes[i])

# 17. Faça um programa que leia uma lista de números e exiba apenas os números que são divisíveis por 3 utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
for i in range(qtd):
    if numeros[i] % 3 == 0:
        print(numeros[i])

# 18. Crie um programa que leia uma lista de nomes e exiba apenas os nomes que possuem mais de uma palavra utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de nomes : '))
nomes = []
for i in range(qtd):
    nome = input('Digite um nome : ')
    nomes.append(nome)
for i in range(qtd):
    if len(nomes[i].split()) > 1:
        print(nomes[i])

# 19. Faça um programa que leia uma lista de números e exiba a soma dos números que estão nas posições ímpares da lista utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de números : '))
numeros = []
for i in range(qtd):
    numero = int(input('Digite um número : '))
    numeros.append(numero)
soma = 0
for i in range(qtd):
    if i % 2 != 0:
        soma += numeros[i]
print(soma)

# 20. Crie um programa que leia uma lista de nomes e exiba apenas os nomes que possuem a letra "u" em qualquer posição utilizando o laço de repetição for.
qtd = int(input('Digite a quantidade de nomes : '))
nomes = []
for i in range(qtd):
    nome = input('Digite um nome : ')
    nomes.append(nome)
for i in range(qtd):
    if 'u' in nomes[i]:
        print(nomes[i])
