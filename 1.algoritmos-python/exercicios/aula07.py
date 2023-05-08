# 1. Crie um algoritmo que verifique se um número é par ou ímpar.
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')

# 2. Crie um algoritmo que verifique se um número é múltiplo de 3, 5, 7 ou 11.
num = int(input('Digite um número: '))
if num % 3 == 0:
    print('O número é múltiplo de 3!')
elif num % 5 == 0:
    print('O número é múltiplo de 5!')
elif num % 7 == 0:
    print('O número é múltiplo de 7!')
elif num % 11 == 0:
    print('O número é múltiplo de 11!')
else:
    print('O número não é múltiplo de 3, 5, 7 ou 11!')

# 3. Crie um algoritmo que verifique se um número é múltiplo de 3, 5 e 7.
num = int(input('Digite um número: '))
if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
    print('O número é múltiplo de 3, 5 e 7!')
else:
    print('O número não é múltiplo de 3, 5 e 7!')

# 4. Crie um algoritmo que verifique se um número é múltiplo de 3 e 5.
num = int(input('Digite um número: '))
if num % 3 == 0 and num % 5 == 0:
    print('O número é múltiplo de 3 e 5!')
else:
    print('O número não é múltiplo de 3 e 5!')

# 5. Crie um algoritmo que verifique se um número é múltiplo de 3 e 7.
num = int(input('Digite um número: '))
if num % 3 == 0 and num % 7 == 0:
    print('O número é múltiplo de 3 e 7!')
else:
    print('O número não é múltiplo de 3 e 7!')

# 6. Crie um algoritmo que verifique se um número é múltiplo de 5 e 7.
num = int(input('Digite um número: '))
if num % 5 == 0 and num % 7 == 0:
    print('O número é múltiplo de 5 e 7!')
else:
    print('O número não é múltiplo de 5 e 7!')

# 7. Crie um algoritmo que verifique se um número é múltiplo de 3 ou 5.
num = int(input('Digite um número: '))
if num % 3 == 0 or num % 5 == 0:
    print('O número é múltiplo de 3 ou 5!')
else:
    print('O número não é múltiplo de 3 ou 5!')

# 8. Crie um algoritmo que verifique se um número é múltiplo de 3 ou 7.
num = int(input('Digite um número: '))
if num % 3 == 0 or num % 7 == 0:
    print('O número é múltiplo de 3 ou 7!')
else:
    print('O número não é múltiplo de 3 ou 7!')

# 9. Crie um algoritmo que verifique se um número é múltiplo de 5 ou 7.
num = int(input('Digite um número: '))
if num % 5 == 0 or num % 7 == 0:
    print('O número é múltiplo de 5 ou 7!')
else:
    print('O número não é múltiplo de 5 ou 7!')

# 10. Crie um algoritmo que verifique se um número é múltiplo de 3 e não é múltiplo de 5.
num = int(input('Digite um número: '))
if num % 3 == 0 and not num % 5 == 0:
    print('O número é múltiplo de 3 e não é 5!')
else:
    print('O número não é múltiplo de 3 e não é 5!')

# 11. Crie um algoritmo que verifique se um número não é múltiplo de 3 e é múltiplo de 5.
num = int(input('Digite um número: '))
if not num % 3 == 0 and num % 5 == 0:
    print('O número não é múltiplo de 3 e é 5!')
else:
    print('O número não é múltiplo de 3 e não é 5!')

# 12. Crie um algoritmo que verifique se um número é múltiplo de 3 e não é múltiplo de 7.
num = int(input('Digite um número: '))
if num % 3 == 0 and not num % 7 == 0:
    print('O número é múltiplo de 3 e não é 7!')
else:
    print('O número não é múltiplo de 3 e não é 7!')

# 13. Crie um algoritmo que verifique se um número não é múltiplo de 3 e é múltiplo de 7.
num = int(input('Digite um número: '))
if not num % 3 == 0 and num % 7 == 0:
    print('O número não é múltiplo de 3 e é 7!')
else:
    print('O número não é múltiplo de 3 e não é 7!')

# 14. Crie um algoritmo que verifique se um número é múltiplo de 5 e não é múltiplo de 7.
num = int(input('Digite um número: '))
if num % 5 == 0 and not num % 7 == 0:
    print('O número é múltiplo de 5 e não é 7!')
else:
    print('O número não é múltiplo de 5 e não é 7!')

# 15. Crie um algoritmo que verifique se um número é múltiplo de 3 e seja par.
num = int(input('Digite um número: '))
if num % 3 == 0 and num % 2 == 0:
    print('O número é múltiplo de 3 e é par!')
else:
    print('O número não é múltiplo de 3 e não é par!')

# 16. Crie um algoritmo que verifique se um número é múltiplo de 3 e não seja par.
num = int(input('Digite um número: '))
if num % 3 == 0 and not num % 2 == 0:
    print('O número é múltiplo de 3 e não é par!')
else:
    print('O número não é múltiplo de 3 e não é par!')

# 17. Crie um algoritmo que verifique se um número é múltiplo de 3 e seja ímpar.
num = int(input('Digite um número: '))
if num % 3 == 0 and num % 2 != 0:
    print('O número é múltiplo de 3 e é ímpar!')
else:
    print('O número não é múltiplo de 3 e não é ímpar!')

# 18. Crie um algoritmo que verifique se um número é múltiplo de 3 e não seja ímpar.
num = int(input('Digite um número: '))
if num % 3 == 0 and not num % 2 != 0:
    print('O número é múltiplo de 3 e não é ímpar!')
else:
    print('O número não é múltiplo de 3 e não é ímpar!')

# 19. Crie um algoritmo que verifique se um número é múltiplo de 5 e seja par.
num = int(input('Digite um número: '))
if num % 5 == 0 and num % 2 == 0:
    print('O número é múltiplo de 5 e é par!')
else:
    print('O número não é múltiplo de 5 e não é par!')

# 20. Crie um algoritmo que verifique se um número é múltiplo de 5 e não seja par.
num = int(input('Digite um número: '))
if num % 5 == 0 and not num % 2 == 0:
    print('O número é múltiplo de 5 e não é par!')
else:
    print('O número não é múltiplo de 5 e não é par!')

# 21. Crie um algoritmo que verifique se um número é múltiplo de 5 e seja ímpar.
num = int(input('Digite um número: '))
if num % 5 == 0 and num % 2 != 0:
    print('O número é múltiplo de 5 e é ímpar!')
else:
    print('O número não é múltiplo de 5 e não é ímpar!')

# 22. Crie um algoritmo que verifique se um número é múltiplo de 5 e não seja ímpar.
num = int(input('Digite um número: '))
if num % 5 == 0 and not num % 2 != 0:
    print('O número é múltiplo de 5 e não é ímpar!')
else:
    print('O número não é múltiplo de 5 e não é ímpar!')

# 23. Crie um algoritmo que verifique se uma palavra possui qualquer vogal.
palavra = input('Digite uma palavra: ')
if 'a' in palavra or 'e' in palavra or 'i' in palavra or 'o' in palavra or 'u' in palavra:
    print('A palavra possui vogal!')
else:
    print('A palavra não possui vogal!')

# 24. Crie um algoritmo que verifique se uma palavra não possui qualquer vogal.
palavra = input('Digite uma palavra: ')
if not 'a' in palavra and not 'e' in palavra and not 'i' in palavra and not 'o' in palavra and not 'u' in palavra:
    print('A palavra não possui vogal!')
else:
    print('A palavra possui vogal!')

# 25. Crie uma lista vazia e adicione os números 10, 20 e 30 utilizando o método append.
lista = []
lista.append(10)
lista.append(20)
lista.append(30)
print(lista)

# 26. Crie uma lista com os números 10, 20 e 30. Utilize o método pop para remover o último elemento da lista.
lista = [10, 20, 30]
lista.pop()
print(lista)

# 27. Crie uma lista com os números 30, 20 e 10. Utilize o método sort para ordenar a lista em ordem crescente.
lista = [30, 20, 10]
lista.sort()
print(lista)

# 28. Crie uma lista com os números 10, 20 e 30. Utilize o método reverse para inverter a ordem dos elementos na lista.
lista = [10, 20, 30]
lista.reverse()
print(lista)

# 29. Crie uma lista com os nomes "João", "Maria" e "Ana". Utilize a função len para saber quantos nomes há na lista.
lista = ['João', 'Maria', 'Ana']
print(len(lista))

# 30. Crie uma lista com os números 10, 20 e 30. Utilize a condição if para verificar se o número 20 está na lista.
lista = [10, 20, 30]
if 20 in lista:
    print('O número 20 está na lista!')
else:
    print('O número 20 não está na lista!')

# 31. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Utilize a condição if para verificar se a palavra "avião" está na lista.
lista = ['casa', 'carro', 'bicicleta', 'moto']
if 'avião' in lista:
    print('A palavra "avião" está na lista!')
else:
    print('A palavra "avião" não está na lista!')

# 32. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Utilize a condição if para verificar se a palavra "carro" está na lista e exibir uma mensagem.
lista = ['casa', 'carro', 'bicicleta', 'moto']
if 'carro' in lista:
    print('A palavra "carro" está na lista!')
else:
    print('A palavra "carro" não está na lista!')

# 33. Crie uma lista com os números 10, 20 e 30. Utilize a condição if para verificar se a soma dos números é maior que 50.
lista = [10, 20, 30]
soma = lista[0] + lista[1] + lista[2]
if soma > 50:
    print('A soma dos números é maior que 50!')
else:
    print('A soma dos números não é maior que 50!')

# 34. Crie uma lista com os números 10, 20 e 30. Utilize a condição else para exibir uma mensagem caso o número 40 não esteja na lista.
lista = [10, 20, 30]
if 40 in lista:
    print('O número 40 está na lista!')
else:
    print('O número 40 não está na lista!')

# 35. Crie uma lista com as palavras "vermelho", "azul" e "verde". Utilize o método sort para ordenar a lista em ordem alfabética.
lista = ['vermelho', 'azul', 'verde']
lista.sort()
print(lista)

# 36. Crie uma lista com os números 10, 20 e 30. Utilize o método pop para remover o elemento com índice 1.
lista = [10, 20, 30]
lista.pop(1)
print(lista)

# 37. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Utilize o método reverse para inverter a ordem das palavras na lista.
lista = ['casa', 'carro', 'bicicleta', 'moto']
lista.reverse()
print(lista)

# 38. Crie uma lista vazia e adicione o nome "João" utilizando o método append.
lista = []
lista.append('João')
print(lista)

# 39. Crie uma lista com os números 10, 20 e 30. Utilize o método pop para remover o primeiro elemento da lista.
lista = [10, 20, 30]
lista.pop(0)
print(lista)

# 40. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Utilize a condição if para verificar se a palavra "carro" está na lista e, se estiver, utilize o método pop para removê-la.
lista = ['casa', 'carro', 'bicicleta', 'moto']
if 'carro' in lista:
    lista.pop(1)
print(lista)

# 41. Crie uma lista com os números 10, 20 e 30. Utilize a função len para saber quantos elementos há na lista.
lista = [10, 20, 30]
print(len(lista))

# 42. Crie uma lista com os números 10, 20 e 30. Utilize a condição if para verificar se o número 40 está na lista e exibir uma mensagem.
lista = [10, 20, 30]
if 40 in lista:
    print('O número 40 está na lista!')
else:
    print('O número 40 não está na lista!')

# 43. Crie uma lista com as palavras "vermelho", "azul" e "verde". Utilize o método pop para remover o último elemento da lista.
lista = ['vermelho', 'azul', 'verde']
lista.pop(2)
print(lista)

# 44. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Utilize o método sort para ordenar a lista em ordem reversa.
lista = ['casa', 'carro', 'bicicleta', 'moto']
lista.sort(reverse=True)
print(lista)

# 45. Crie uma lista com os números 10, 20 e 30. Acesse o primeiro elemento da lista utilizando o índice.
lista = [10, 20, 30]
print(lista[0])

# 46. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Acesse o terceiro elemento da lista utilizando o índice.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[2])

# 47. Crie uma lista com os números 10, 20 e 30. Divida a lista em duas partes iguais utilizando índices.
lista = [10, 20, 30]
print(lista[:2])
print(lista[1:])

# 48. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Divida a lista em duas partes iguais utilizando índices.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[:2])
print(lista[2:])

# 49. Crie uma lista com os números 10, 20 e 30. Acesse o último elemento da lista utilizando o índice.
lista = [10, 20, 30]
print(lista[-1])

# 50. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Acesse o primeiro elemento da lista utilizando o índice.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[0])

# 51. Crie uma lista com os números 10, 20 e 30. Divida a lista em três partes iguais utilizando índices.
lista = [10, 20, 30]
print(lista[:1])
print(lista[1:])

# 52. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Divida a lista em quatro partes iguais utilizando índices.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[:1])
print(lista[1:2])
print(lista[2:3])
print(lista[3:])

# 53. Crie uma lista com os números 10, 20 e 30. Acesse o segundo elemento da lista utilizando o índice.
lista = [10, 20, 30]
print(lista[1])

# 54. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Acesse o último elemento da lista utilizando o índice.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[len(lista) - 1])
print(lista[-1])

# 55. Crie uma lista com os números 10, 20 e 30. Divida a lista em duas partes, a primeira contendo o primeiro e segundo elementos e a segunda contendo o terceiro elemento.
lista = [10, 20, 30]
print(lista[:2])
print(lista[2:])

# 56. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Divida a lista em duas partes, a primeira contendo o primeiro e segundo elementos e a segunda contendo o terceiro e quarto elementos.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[:2])
print(lista[2:])

# 57. Crie uma lista com os números 10, 20 e 30. Acesse o último elemento da lista utilizando índice negativo.
lista = [10, 20, 30]
print(lista[-1])

# 58. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Acesse o primeiro elemento da lista utilizando índice negativo.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[-4])

# 59. Crie uma lista com os números 10, 20 e 30. Divida a lista em três partes, a primeira contendo o primeiro elemento, a segunda contendo o segundo elemento e a terceira contendo o terceiro elemento.
lista = [10, 20, 30]
print(lista[:1])
print(lista[1:2])
print(lista[2:])

# 60. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Divida a lista em quatro partes, a primeira contendo o primeiro elemento, a segunda contendo o segundo elemento, a terceira contendo o terceiro elemento e a quarta contendo o quarto elemento.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[:1])
print(lista[1:2])
print(lista[2:3])
print(lista[3:])

# 61. Crie uma lista com os números 10, 20 e 30. Acesse o segundo elemento da lista utilizando índice negativo.
lista = [10, 20, 30]
print(lista[-2])

# 62. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Acesse o segundo elemento da lista utilizando índice negativo.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[-3])

# 63. Crie uma lista com os números 10, 20 e 30. Divida a lista em duas partes, a primeira contendo o primeiro elemento e a segunda contendo o segundo e terceiro elementos.
lista = [10, 20, 30]
print(lista[:1])
print(lista[1:])

# 64. Crie uma lista com as palavras "casa", "carro", "bicicleta" e "moto". Divida a lista em duas partes, a primeira contendo o primeiro e terceiro elementos e a segunda contendo o segundo e quarto elementos.
lista = ['casa', 'carro', 'bicicleta', 'moto']
print(lista[0] + lista[2])
print(lista[1] + lista[3])

# 65. Crie uma string com a frase "O rato roeu a roupa do rei de Roma". Acesse o primeiro caractere da string utilizando o índice.
frase = 'O rato roeu a roupa do rei de Roma'
print(frase[0])

# 66. Crie uma string com a palavra "Python". Acesse o último caractere da string utilizando o índice.
palavra = 'Python'
print(palavra[len(palavra) - 1])
print(palavra[-1])

# 67. Crie uma string com a frase "Amanhã é sexta-feira". Acesse o quarto caractere da string utilizando o índice.
frase = 'Amanhã é sexta-feira'
print(frase[3])

# 68. Crie uma string com a palavra "Futebol". Acesse o segundo caractere da string utilizando o índice.
palavra = 'Futebol'
print(palavra[1])

# 69. Crie uma string com a frase "O tempo está bom hoje". Utilize a função len para contar quantos caracteres tem na string.
frase = 'O tempo está bom hoje'
print(len(frase))

# 70. Crie uma string com a palavra "Abacaxi". Utilize a função len para contar quantos caracteres tem na string.
palavra = 'Abacaxi'
print(len(palavra))

# 71. Crie uma string com a frase "O gato mia quando está com fome". Acesse o último caractere da string utilizando índice negativo.
frase = 'O gato mia quando está com fome'
print(frase[-1])

# 72. Crie uma string com a palavra "Pneumático". Acesse o terceiro caractere da string utilizando índice negativo.
palavra = 'Pneumático'
indice = (len(palavra) - 3) * -1
print(palavra[indice])

# 73. Crie uma string com a frase "Amanhã é dia de ir ao cinema". Divida a string em duas partes iguais utilizando índices.
frase = 'Amanhã é dia de ir ao cinema'
print(frase[:len(frase) // 2])
print(frase[len(frase) // 2:])

# 74. Crie uma string com a palavra "Paralelepípedo". Divida a string em duas partes iguais utilizando índices.
palavra = 'Paralelepípedo'
print(palavra[:len(palavra) // 2])
print(palavra[len(palavra) // 2:])

# 75. Crie uma string com a frase "Os pássaros voam no céu azul". Acesse o primeiro caractere da palavra "céu" utilizando o índice.
frase = 'Os pássaros voam no céu azul'
print(frase[20])

# 76. Crie uma string com a palavra "Hipopótamo". Acesse o último caractere da palavra utilizando o índice negativo.
palavra = 'Hipopótamo'
print(palavra[-1])

# 77. Crie uma string com a frase "O cachorro late quando vê um desconhecido". Divida a string em três partes iguais utilizando índices.
frase = 'O cachorro late quando vê um desconhecido'
print(frase[:len(frase) // 3])
print(frase[len(frase) // 3:len(frase) // 3 * 2])
print(frase[len(frase) // 3 * 2:])

# 78. Crie uma string com a palavra "Estatística". Acesse o segundo caractere da palavra utilizando o índice negativo.
palavra = 'Estatística'
print(palavra[-8])

# 79. Crie uma string com a frase "Eu gosto de sorvete de chocolate". Utilize a função len para contar quantas palavras tem na string.
frase = 'Eu gosto de sorvete de chocolate'
print(len(frase.split()))

# 80. Crie uma string com a palavra "Azeitona". Utilize a função len para contar quantas vogais tem na string.
palavra = 'Azeitona'
soma = palavra.count('a') + palavra.count('e') + palavra.count('i') + palavra.count('o') + palavra.count('u')
print(soma)

# 81. Crie uma string com a frase "O pássaro canta na árvore". Acesse o último caractere da palavra "árvore" utilizando índice negativo.
frase = 'O pássaro canta na árvore'
print(frase[-1])

# 82. Crie uma string com a palavra "Papagaio". Divida a string em duas partes, a primeira contendo os dois primeiros caracteres e a segunda contendo os quatro últimos caracteres.
palavra = 'Papagaio'
print(palavra[:2])
print(palavra[-4:])

# 83. Crie uma string com a frase "O sol brilha no céu". Acesse o primeiro caractere da palavra "brilha" utilizando o índice.
frase = 'O sol brilha no céu'
palavras = frase.split()
print(palavras[2][0])

# 84. Crie uma string com a palavra "Pneumoultramicroscopicossilicovulcanoconiótico". Utilize a função len para contar quantas letras tem na palavra.
palavra = 'Pneumoultramicroscopicossilicovulcanoconiótico'
print(len(palavra))

# 85. Dado um nome completo em uma string separada por espaço, verifique se a pessoa tem um sobrenome. Use o método split e uma condição if.
nome = 'João da Silva'
palavras = nome.split()
if palavras > 1:
    print('Tem sobrenome')
else:
    print('Não tem sobrenome')

# 86. Dada uma lista de palavras, junte-as em uma única string separada por vírgulas. Use o método join.
palavras = ['azul', 'verde', 'amarelo', 'vermelho']
print(','.join(palavras))

# 87. Dada uma string com a frase "O cachorro correu atrás do gato", separe cada palavra em uma lista. Use o método split.
frase = 'O cachorro correu atrás do gato'
print(frase.split())

# 88. Dado um número inteiro, verifique se é um número par ou ímpar. Converta-o para uma string e verifique o último caractere. Use uma condição if.
numero = 5
if numero % 2 == 0:
    print('Par')
else:
    print('Ímpar')

string = str(numero)
print(string[-1])

# 89. Dada uma lista com as cores "azul", "verde", "amarelo" e "vermelho", junte-as em uma única string separada por vírgulas e adicione a palavra "e" antes da última cor. Use o método join.
cores = ['azul', 'verde', 'amarelo', 'vermelho']
print(','.join(cores[:-1]) + ' e ' + cores[-1])

# 90. Dada uma string com a frase "Eu amo programar em Python", separe cada palavra em uma lista e verifique se a palavra "Python" está na lista. Use o método split e uma condição if.
frase = 'Eu amo programar em Python'
palavras = frase.split()
if 'Python' in palavras:
    print('Python está na lista')

# 91. Dado um número real, verifique se é positivo ou negativo. Converta-o para uma string e verifique o primeiro caractere. Use uma condição if.
numero = -5.5
if numero > 0:
    print('Positivo')
else:
    print('Negativo')
string = str(numero)
print(string[0])

# 92. Dada uma lista com os números 2, 4, 6 e 8, junte-os em uma única string separada por vírgulas e adicione a palavra "e" antes do último número. Use o método join.
numeros = [2, 4, 6, 8]
print(','.join(str(numeros[:-1])) + ' e ' + str(numeros[-1]))

# 93. Dada uma string com a frase "A minha casa é azul", separe cada palavra em uma lista e verifique se a palavra "vermelho" está na lista. Use o método split e uma condição if.
frase = 'A minha casa é azul'
palavras = frase.split()
if 'vermelho' in palavras:
    print('Vermelho está na lista')

# 94. Dado um número inteiro, verifique se é maior ou menor que 10. Converta-o para uma string e verifique o primeiro caractere. Use uma condição if.
numero = 5
if numero > 10:
    print('Maior que 10')
else:
    print('Menor que 10')
string = str(numero)
print(string[0])

# 95. Dada uma lista com as frutas "maçã", "banana", "laranja" e "abacaxi", junte-as em uma única string separada por vírgulas e adicione a palavra "e" antes da última fruta. Use o método join.
frutas = ['maçã', 'banana', 'laranja', 'abacaxi']
print(','.join(frutas[:-1]) + ' e ' + frutas[-1])

# 96. Dada uma string com a frase "Eu gosto de andar de bicicleta", separe cada palavra em uma lista e verifique se a palavra "bicicleta" está na lista. Use o método split e uma condição if.
frase = 'Eu gosto de andar de bicicleta'
palavras = frase.split()
if 'bicicleta' in palavras:
    print('Bicicleta está na lista')

# 97. Dado um número real, verifique se é um número inteiro ou um número decimal. Converta-o para uma string e verifique se contém o caractere ".". Use uma condição if.
numero = 5.5
if numero % 1 == 0:
    print('Inteiro')
else:
    print('Decimal')

string = str(numero)
if '.' in string:
    print('Decimal')

# 98. Dada uma lista com os números 3, 6, 9 e 12, junte-os em uma única string separada por vírgulas e adicione a palavra "e" antes do último número. Use o método join.
numeros = [3, 6, 9, 12]
print(','.join(str(numeros[:-1])) + ' e ' + str(numeros[-1]))

# 99. Dada uma string com a frase "O meu carro é vermelho", separe cada palavra em uma lista e verifique se a palavra "verde" está na lista. Use o método split e uma condição if.
frase = 'O meu carro é vermelho'
palavras = frase.split()
if 'verde' in palavras:
    print('Verde está na lista')

# 100. Dado um número inteiro, verifique se é positivo, negativo ou zero. Converta-o para uma string e verifique o primeiro caractere. Use uma condição if.
numero = 5
if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Zero')
string = str(numero)
print(string[0])

# 101. Dada uma lista com as cores "branco", "preto", "cinza" e "marrom", junte-as em uma única string separada por vírgulas e adicione a palavra "ou" antes da última cor. Use o método join.
cores = ['branco', 'preto', 'cinza', 'marrom']
print(','.join(cores[:-1]) + ' ou ' + cores[-1])

# 102. Dada uma string com a frase "Eu moro em São Paulo", separe cada palavra em uma lista e verifique se a palavra "Rio de Janeiro" está na lista. Use o método split e uma condição if.
frase = 'Eu moro em São Paulo'
palavras = frase.split()
if 'Rio de Janeiro' in palavras:
    print('Rio de Janeiro está na lista')

# 103. Dado um número real, verifique se é um número positivo, negativo ou zero. Converta-o para uma string e verifique o primeiro caractere. Use uma condição if.
numero = -5.5
if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Zero')
string = str(numero)
print(string[0])

# 104. Dada uma lista com as cidades "São Paulo", "Rio de Janeiro", "Belo Horizonte" e "Curitiba", junte-as em uma única string separada por vírgulas e adicione a palavra "e" antes da última cidade. Use o método join.
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
print(','.join(cidades[:-1]) + ' e ' + cidades[-1])
