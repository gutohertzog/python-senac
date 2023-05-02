import random
# 1. Imprima números de 1 a 10 usando um loop while.
i = 1
while i <= 10:
    print(i)

# 2. Peça ao usuário para digitar um número e imprima todos os números de 0 até o número digitado.
num = int(input('Digite um número : '))
i = 0
while i <= num:
    print(i)
    i += 1

# 3. Peça ao usuário para digitar uma palavra e imprima cada letra em uma linha usando um loop while.
palavra = input('Digite uma palavra : ')
i = 0
while i < len(palavra):
    print(palavra[i])
    i += 1

# 4. Peça ao usuário para digitar uma palavra e imprima a palavra ao contrário usando um loop while.
palavra = input('Digite uma palavra : ')
i = len(palavra) - 1
while i >= 0:
    print(palavra[i])
    i -= 1

# 5. Peça ao usuário para digitar um número e imprima a soma de todos os números de 1 até o número digitado.
num = int(input('Digite um número : '))
i = 1
soma = 0
while i <= num:
    soma += i
    i += 1

# 6. Peça ao usuário para digitar um número e imprima todos os números pares de 0 até o número digitado.
num = int(input('Digite um número : '))
i = 0
while i <= num:
    if i % 2 == 0:
        print(i)
    i += 1

# 7. Peça ao usuário para digitar um número e imprima todos os números ímpares de 0 até o número digitado.
num = int(input('Digite um número : '))
i = 0
while i <= num:
    if i % 2 == 1:
        print(i)
    i += 1

# 8. Peça ao usuário para digitar uma palavra e imprima o número de letras da palavra usando um loop while.
palavra = input('Digite uma palavra : ')
i = 0
contador = 0
while i < len(palavra):
    if palavra[i] != ' ':
        contador += 1
    i += 1
print(contador)

# 9. Imprima a tabuada do número 5 usando um loop while.
i = 1
while i <= 10:
    print(f'5 x {i} = {5 * i}')
    i += 1

# 10. Peça ao usuário para digitar um número e imprima se ele é primo ou não usando um loop while.
num = int(input('Digite um número : '))
i = 2
primo = True
while i < num:
    if num % i == 0:
        primo = False
    i += 1
if primo:
    print('É primo')
else:
    print('Não é primo')

# 11. Peça ao usuário para digitar uma palavra e imprima apenas as vogais da palavra usando um loop while.
palavra = input('Digite uma palavra : ')
i = 0
while i < len(palavra):
    if palavra[i] in 'aeiou':
        print(palavra[i])
    i += 1

# 12. Peça ao usuário para digitar uma palavra e imprima apenas as consoantes da palavra usando um loop while.
palavra = input('Digite uma palavra : ')
i = 0
while i < len(palavra):
    if palavra[i] not in 'aeiou':
        print(palavra[i])
    i += 1

# 13. Imprima todos os números de 100 até 0 em ordem decrescente usando um loop while.
i = 100
while i >= 0:
    print(i)
    i -= 1

# 14. Peça ao usuário para digitar um número e imprima todos os números pares de 1 até o número digitado usando um loop while.
num = int(input('Digite um número : '))
i = 1
while i <= num:
    if i % 2 == 0:
        print(i)
    i += 1

# 15. Peça ao usuário para digitar um número e imprima a soma de todos os números pares de 1 até o número digitado usando um loop while.
num = int(input('Digite um número : '))
i = 1
soma = 0
while i <= num:
    if i % 2 == 0:
        soma += i
    i += 1
print(soma)

# 16. Peça ao usuário para digitar um número e imprima todos os números ímpares de 1 até o número digitado usando um loop while.
num = int(input('Digite um número : '))
i = 1
while i <= num:
    if i % 2 == 1:
        print(i)
    i += 1

# 17. Peça ao usuário para digitar um número e imprima a soma de todos os números ímpares de 1 até o número digitado usando um loop while.
num = int(input('Digite um número : '))
i = 1
soma = 0
while i <= num:
    if i % 2 == 1:
        soma += i
    i += 1
print(soma)

# 18. Peça ao usuário para digitar um texto e imprima a primeira letra de cada palavra usando um loop while.
texto = input('Digite um texto : ')
i = 0
while i < len(texto):
    if i == 0:
        print(texto[i])
    elif texto[i] == ' ':
        print(texto[i + 1])
    i += 1

# 19. Peça ao usuário para digitar um número e imprima a sequência de Fibonacci até o número digitado usando um loop while.
num = int(input('Digite um número : '))
i = 0
anterior = 0
atual = 1
while i <= num:
    print(atual)
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    i += 1

# 20. Peça ao usuário para digitar uma palavra e imprima a palavra sem as vogais usando um loop while.
palavra = input('Digite uma palavra : ')
i = 0
while i < len(palavra):
    if palavra[i] not in 'aeiou':
        print(palavra[i])
    i += 1

# 21. Peça ao usuário para digitar uma palavra e imprima a palavra sem as consoantes usando um loop while.
palavra = input('Digite uma palavra : ')
i = 0
while i < len(palavra):
    if palavra[i] in 'aeiou':
        print(palavra[i])
    i += 1

# 22. Peça ao usuário para digitar uma palavra e imprima cada letra duas vezes usando um loop while. Exemplo: se o usuário digitar "casa", deve mostrar "ccaassaa".
palavra = input('Digite uma palavra : ')
i = 0
while i < len(palavra):
    print(palavra[i] * 2)
    i += 1

# 23. Peça ao usuário para digitar uma palavra e imprima a palavra com cada letra alternando entre maiúscula e minúscula usando um loop while. Exemplo: se o usuário digitar "gandalf", a saída deve ser "GaNdAlF".
palavra = input('Digite uma palavra : ')
i = 0
while i < len(palavra):
    if i % 2 == 0:
        print(palavra[i].upper())
    else:
        print(palavra[i].lower())
    i += 1

# 24. Gere uma lista de números aleatória (módulo random) e imprima a lista em ordem crescente usando um loop while. Não use os métodos de ordenação built-in do Python.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0

# ordenação por seleção
while i < len(lista):
    j = 0
    while j < len(lista):
        if lista[i] < lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
        j += 1
    i += 1
print(lista)

# 25. Gere uma lista de números aleatória (módulo random) e imprima a lista em ordem decrescente usando um loop while. Não use os métodos de ordenação built-in do Python.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0

# ordenação por seleção
while i < len(lista):
    j = 0
    while j < len(lista):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
        j += 1
    i += 1
print(lista)

# 26. Peça ao usuário para digitar uma palavra e imprima a palavra ao contrário usando um loop while e uma lista.
palavra = input('Digite uma palavra : ')
lista = []
i = len(palavra) - 1
while i >= 0:
    lista.append(palavra[i])
    i -= 1
print(lista)

# 27. Gere uma lista de números aleatória (módulo random) e imprima apenas os números pares da lista usando um loop while.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        print(lista[i])
    i += 1

# 28. Gere uma lista de números aleatória (módulo random) e imprima apenas os números ímpares da lista usando um loop while.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] % 2 == 1:
        print(lista[i])
    i += 1

# 29. Gere uma lista de números aleatória (módulo random) e imprima a média dos números usando um loop while.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0
soma = 0
while i < len(lista):
    soma += lista[i]
    i += 1
print(soma / len(lista))

# 30. Gere uma lista de números aleatória (módulo random) e imprima a soma dos números usando um loop while.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0
soma = 0
while i < len(lista):
    soma += lista[i]
    i += 1
print(soma)

# 31. Gere uma lista de números aleatória (módulo random) e imprima o maior número da lista usando um loop while.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0
maior = lista[0]
while i < len(lista):
    if lista[i] > maior:
        maior = lista[i]
    i += 1
print(maior)

# 32. Gere uma lista de números aleatória (módulo random) e imprima o menor número da lista usando um loop while.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0
menor = lista[0]
while i < len(lista):
    if lista[i] < menor:
        menor = lista[i]
    i += 1
print(menor)

# 33. Gere uma lista de números aleatória (módulo random) e imprima apenas os números que são múltiplos de 3 usando um loop while.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] % 3 == 0:
        print(lista[i])
    i += 1

# 34. Gere uma lista de números aleatória (módulo random) e imprima apenas os números que são múltiplos de 5 usando um loop while.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] % 5 == 0:
        print(lista[i])
    i += 1

# 35. Peça ao usuário para digitar uma palavra e imprima apenas as letras que aparecem mais de uma vez na palavra usando um loop while.
palavra = input('Digite uma palavra : ')
lista = []
i = 0
while i < len(palavra):
    lista.append(palavra[i])
    i += 1
i = 0
while i < len(lista):
    j = 0
    cont = 0
    while j < len(lista):
        if lista[i] == lista[j]:
            cont += 1
        j += 1
    if cont > 1:
        print(lista[i])
    i += 1

# 36. Gere uma lista de números aleatória (módulo random) e imprima a lista sem números duplicados usando um loop while.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(0, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    j = i + 1
    while j < len(lista):
        if lista[i] == lista[j]:
            lista.pop(j)
        j += 1
    i += 1
print(lista)

# 37. Escreva um programa que imprima os números de 1 a 10, pulando o número 7 usando o continue.
i = 1
while i <= 10:
    if i == 7:
        i += 1
        continue
    print(i)
    i += 1

# 38. Escreva um programa que solicita ao usuário que digite um número e verifica se o número é par ou ímpar. Se for ímpar, o programa deve continuar solicitando ao usuário que digite um número até que um número par seja inserido.
num = int(input('Digite um número : '))
while num % 2 == 1:
    num = int(input('Digite um número : '))
print('Número par')

# 39. Escreva um programa que solicita ao usuário que digite uma senha. O programa deve continuar solicitando ao usuário que digite a senha até que a senha correta seja inserida. Use o break para sair do loop quando a senha correta for inserida.
senha = input('Digite uma senha : ')
while True:
    senha = input('Digite uma senha : ')
    if senha == '123':
        break
print('Senha correta')

# 40. Escreva um programa que solicita ao usuário que digite um número. O programa deve continuar solicitando ao usuário que digite um número até que um número divisível por 7 seja inserido.
num = int(input('Digite um número : '))
while True:
    num = int(input('Digite um número : '))
    if num % 7 == 0:
        break
print('Número divisível por 7')

# 41. Escreva um programa que solicita ao usuário que digite uma palavra. O programa deve continuar solicitando ao usuário que digite uma palavra até que a palavra "fim" seja inserida. Use o break para sair do loop quando a palavra "fim" for inserida.
palavra = input('Digite uma palavra : ')
while True:
    palavra = input('Digite uma palavra : ')
    if palavra == 'fim':
        break
print('Fim')

# 42. Escreva um programa que imprima os números de 1 a 20. Se o número for divisível por 3, o programa deve imprimir "Fizz" em vez do número. Se o número for divisível por 5, o programa deve imprimir "Buzz" em vez do número. Se o número for divisível por 3 e 5, o programa deve imprimir "FizzBuzz" em vez do número. Use o continue para evitar a impressão de números que são divisíveis por 3 ou 5.
i = 1
while i <= 20:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        i += 1
        continue
    if i % 3 == 0:
        print('Fizz')
        i += 1
        continue
    if i % 5 == 0:
        print('Buzz')
        i += 1
        continue
    print(i)
    i += 1

# 43. Escreva um programa que solicita ao usuário que digite uma palavra. O programa deve imprimir a palavra invertida, mas parar de imprimir assim que chegar na letra "a". Use o break para sair do loop quando a letra "a" for encontrada.
palavra = input('Digite uma palavra : ')
i = len(palavra) - 1
while i >= 0:
    if palavra[i] == 'a':
        break
    print(palavra[i])
    i -= 1

# 44. Escreva um programa que solicita ao usuário que digite um número. O programa deve continuar solicitando ao usuário que digite um número até que um número maior que 100 seja inserido. Use o break para sair do loop quando um número maior que 100 for inserido.
num = int(input('Digite um número : '))
while True:
    num = int(input('Digite um número : '))
    if num > 100:
        break
print('Número maior que 100')

# 45. Escreva um programa que crie uma lista de números aleatórios (módulo random). O programa deve imprimir os números, mas parar de imprimir assim que encontrar um número negativo. Use o break para sair do loop quando um número negativo for encontrado.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(-100, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] < 0:
        break
    print(lista[i])
    i += 1

# 46. Escreva um programa que imprima os números pares de 1 a 10 usando o continue.
i = 0
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i)

# 47. Escreva um programa que solicita ao usuário que digite um número. O programa deve continuar solicitando ao usuário que digite um número até que um número entre 1 e 10 seja inserido. Use o continue para evitar a entrada de números que estão fora desse intervalo.
num = int(input('Digite um número : '))
while True:
    num = int(input('Digite um número : '))
    if num >= 1 and num <= 10:
        break
print('Número entre 1 e 10')

# 48. Escreva um programa que crie uma lista de números aleatórios (módulo random). O programa deve imprimir apenas os números ímpares da lista. Use o continue para evitar a impressão de números pares.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(-100, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        i += 1
        continue
    print(lista[i])
    i += 1

# 49. Escreva um programa que solicita ao usuário que digite uma palavra. O programa deve imprimir a palavra em ordem inversa, mas pular as vogais usando o continue.
palavra = input('Digite uma palavra : ')
i = len(palavra) - 1
while i >= 0:
    if palavra[i] == 'a' or palavra[i] == 'e' or palavra[i] == 'i' or palavra[i] == 'o' or palavra[i] == 'u':
        i -= 1
        continue
    print(palavra[i])
    i -= 1

# 50. Escreva um programa que solicita ao usuário que digite um número. O programa deve continuar solicitando ao usuário que digite um número até que um número entre 1 e 100 seja inserido. Use o continue para evitar a entrada de números que estão fora desse intervalo.
num = int(input('Digite um número : '))
while True:
    num = int(input('Digite um número : '))
    if num >= 1 and num <= 100:
        break
print('Número entre 1 e 100')

# 51. Escreva um programa que solicita ao usuário que digite uma lista de palavras. O programa deve imprimir cada palavra em uma linha separada, mas pular as palavras que contêm a letra "a" usando o continue.
frase = input('Digite várias palavras : ')
palavras = frase.split()
i = 0
while i < len(palavras):
    if 'a' in palavras[i]:
        i += 1
        continue
    print(palavras[i])
    i += 1

# 52. Escreva um programa que crie uma lista de números aleatórios (módulo random). O programa deve imprimir apenas os números pares da lista. Use o continue para evitar a impressão de números ímpares.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(-100, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] % 2 == 1:
        i += 1
        continue
    print(lista[i])
    i += 1

# 53. Escreva um programa que solicita ao usuário que digite um número. O programa deve continuar solicitando ao usuário que digite um número até que um número entre 1 e 10 seja inserido. Quando um número válido for inserido, o programa deve imprimir "Número válido" e sair do loop usando o break.
num = int(input('Digite um número : '))
while True:
    num = int(input('Digite um número : '))
    if num >= 1 and num <= 10:
        break
print('Número válido')

# 54. Escreva um programa que crie uma lista de números aleatórios (módulo random). O programa deve imprimir cada número multiplicado por 2, mas pular os números ímpares usando o continue.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(-100, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] % 2 == 1:
        i += 1
        continue
    print(lista[i] * 2)
    i += 1

# 55. Escreva um programa que solicita ao usuário que digite um número. O programa deve continuar solicitando ao usuário que digite um número até que um número divisível por 5 seja inserido. Quando um número válido for inserido, o programa deve imprimir "Número válido" e sair do loop usando o break.
num = int(input('Digite um número : '))
while True:
    num = int(input('Digite um número : '))
    if num % 5 == 0:
        break
print('Número válido')

# 56. Escreva um programa que crie uma lista de números aleatórios (módulo random). O programa deve imprimir apenas os números maiores que 10. Use o continue para evitar a impressão de números menores ou iguais a 10.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(-100, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] <= 10:
        i += 1
        continue
    print(lista[i])
    i += 1

# 57. Escreva um programa que solicita ao usuário que digite uma sequência de números positivos. O programa deve imprimir a soma dos números inseridos até que o usuário insira um número negativo, momento em que o programa deve parar usando o break.
soma = 0
while True:
    num = int(input('Digite um número : '))
    if num < 0:
        break
    soma += num
print(soma)

# 58. Escreva um programa que solicita ao usuário que digite uma palavra ou frase. O programa deve imprimir o número de vezes que cada letra aparece na palavra ou frase, mas pular a letra "e" usando o continue.
frase = input('Digite uma frase : ')
i = 0
while i < len(frase):
    if frase[i] == 'e':
        i += 1
        continue
    print(frase[i], frase.count(frase[i]))
    i += 1

# 59. Escreva um programa que solicita ao usuário que digite uma lista de números. O programa deve imprimir o maior número da lista usando o break assim que encontrar o primeiro número maior que 10.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(-100, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] > 10:
        break
    i += 1
print(lista[i])

# 60. Escreva um programa que solicita ao usuário que digite uma sequência de números positivos. O programa deve imprimir a média dos números inseridos até que o usuário insira um número negativo, momento em que o programa deve parar usando o break.
soma = 0
i = 0
while True:
    num = int(input('Digite um número : '))
    if num < 0:
        break
    soma += num
    i += 1
print(soma / i)

# 61. Escreva um programa que solicita ao usuário que digite uma lista de palavras. O programa deve imprimir cada palavra em uma linha separada, mas pular as palavras que contêm a letra "o" usando o continue.
frase = input('Digite uma frase : ')
palavras = frase.split()
i = 0
while i < len(palavras):
    if 'o' in palavras[i]:
        i += 1
        continue
    print(palavras[i])
    i += 1

# 62. Escreva um programa que solicita ao usuário que digite uma lista de números. O programa deve imprimir apenas os números que são divisíveis por 3 e 5 usando o continue.
lista = []
i = 0
while i < 10:
    lista.append(random.randint(-100, 100))
    i += 1
print(lista)
i = 0
while i < len(lista):
    if lista[i] % 3 != 0 or lista[i] % 5 != 0:
        i += 1
        continue
    print(lista[i])
    i += 1

# 63. Escreva um programa que solicita ao usuário que digite uma sequência de números positivos. O programa deve imprimir a soma dos números inseridos até que o usuário insira um número maior que 100, momento em que o programa deve parar usando o break.
soma = 0
while True:
    num = int(input('Digite um número : '))
    if num > 100:
        break
    soma += num
print(soma)

# 64. Escreva um programa que solicita ao usuário que digite uma lista de números. O programa deve imprimir a média dos números inseridos, mas pular os números negativos usando o continue. Se o usuário inserir um número maior que 100, o programa deve sair do loop e imprimir uma mensagem de erro usando o break.
soma = 0
i = 0
while True:
    num = int(input('Digite um número : '))
    if num > 100:
        print('Erro')
        break
    if num < 0:
        continue
    soma += num
    i += 1
print(soma / i)

# 65. Escreva um programa que solicita ao usuário que adivinhe um número entre 1 e 10. O programa deve permitir que o usuário faça até 3 tentativas. Se o usuário adivinhar corretamente em qualquer tentativa, o programa deve imprimir "Parabéns, você acertou!". Caso contrário, o programa deve imprimir "Suas tentativas acabaram. O número correto era X", onde X é o número correto.
num = random.randint(1, 10)
i = 0
while i < 3:
    chute = int(input('Digite um número : '))
    if chute == num:
        print('Parabéns, você acertou!')
        break
    i += 1
if i == 3:
    print('Suas tentativas acabaram. O número correto era', num)
