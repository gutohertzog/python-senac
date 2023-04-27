import math

# 1. Crie um programa que peça ao usuário para digitar seu nome e, em seguida, imprima "Olá, [nome do usuário]!".
nome = input('Digite seu nome: ')
print('Olá, {}!'.format(nome))

# 2. Crie um programa que peça ao usuário para digitar sua idade e, em seguida, imprima "Você nasceu em [ano de nascimento]".
idade = int(input('Digite sua idade: '))
print('Você nasceu em {}'.format(2021 - idade))

# 3. Crie um programa que peça ao usuário para digitar um número e, em seguida, imprima o dobro desse número.
numero = int(input('Digite um número: '))
print('O dobro de {} é {}'.format(numero, numero * 2))

# 4. Crie um programa que peça ao usuário para digitar dois números e, em seguida, imprima a soma desses números.
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print('A soma de {} e {} é {}'.format(numero1, numero2, numero1 + numero2))

# 5. Crie um programa que peça ao usuário para digitar um número e, em seguida, imprima o valor absoluto desse número.
numero = int(input('Digite um número: '))
print('O valor absoluto de {} é {}'.format(numero, abs(numero)))

# 6. Crie um programa que peça ao usuário para digitar uma temperatura em graus Celsius e, em seguida, imprima a temperatura em graus Fahrenheit.
celsius = float(input('Digite a temperatura em graus Celsius: '))
print('A temperatura em graus Fahrenheit é {}'.format(celsius * 1.8 + 32))

# 7. Crie um programa que peça ao usuário para digitar sua altura em metros e, em seguida, imprima sua altura em centímetros.
altura = float(input('Digite sua altura em metros: '))
print('Sua altura em centímetros é {}'.format(altura * 100))

# 8. Crie um programa que peça ao usuário para digitar seu peso em quilogramas e, em seguida, imprima seu peso em libras.
peso = float(input('Digite seu peso em quilogramas: '))
print('Seu peso em libras é {}'.format(peso * 2.20462))

# 9. Crie um programa que peça ao usuário para digitar um número e, em seguida, imprima a raiz quadrada desse número.
numero = int(input('Digite um número: '))
print('A raiz quadrada de {} é {}'.format(numero, numero ** 0.5))

# 10. Crie um programa que peça ao usuário para digitar um número e, em seguida, imprima o seu logaritmo na base 10.
numero = int(input('Digite um número: '))
print('O logaritmo de {} na base 10 é {}'.format(numero, math.log10(numero)))

# 11. Crie um programa que peça ao usuário para digitar seu nome e idade, e em seguida, imprima "Olá, [nome do usuário], você tem [idade] anos!".
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print('Olá, {}, você tem {} anos!'.format(nome, idade))

# 12. Crie um programa que peça ao usuário para digitar um número e, em seguida, imprima uma contagem de ocorrência cada número individualmente.
numero = input('Digite um número: ')
print('{} aparece {} vezes'.format(0, numero.count(0)))
print('{} aparece {} vezes'.format(1, numero.count(1)))
print('{} aparece {} vezes'.format(2, numero.count(2)))
print('{} aparece {} vezes'.format(3, numero.count(3)))
print('{} aparece {} vezes'.format(4, numero.count(4)))
print('{} aparece {} vezes'.format(5, numero.count(5)))
print('{} aparece {} vezes'.format(6, numero.count(6)))
print('{} aparece {} vezes'.format(7, numero.count(7)))
print('{} aparece {} vezes'.format(8, numero.count(8)))
print('{} aparece {} vezes'.format(9, numero.count(9)))

# 13. Receba uma string do usuário e exiba-a em letras maiúsculas com a primeira letra em minúscula.
string = input('Digite uma string: ')
print(string.capitalize())

# 14. Receba uma string do usuário e substitua todas as letras "a" por "o".
string = input('Digite uma string: ')
print(string.replace('a', 'o'))

# 15. Receba uma string do usuário e conte quantas vezes a letra "e" aparece.
string = input('Digite uma string: ')
print(string.count('e'))

# 16. Receba uma string do usuário e conte quantas palavras existem nela.
string = input('Digite uma string: ')
print(len(string.split()))

# 17. Receba uma string do usuário e remova todos os espaços em branco.
string = input('Digite uma string: ')
print(string.replace(' ', ''))

# 18. Receba uma string do usuário e remova todos os caracteres que não são letras.
string = input('Digite uma string: ')
print(string.replace(' ', ''))

# 19. Receba uma string do usuário e troque todas as vogais por "*".
string = input('Digite uma string: ')
print(string.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*'))

# 20. Receba uma string do usuário e conte quantas vezes a palavra "python" aparece.
string = input('Digite uma string: ')
print(string.count('python'))

# 21. Receba duas strings do usuário e exiba-as concatenadas.
string1 = input('Digite uma string: ')
string2 = input('Digite outra string: ')
print(string1 + string2)

# 22. Receba uma string do usuário e exiba-a em letras maiúsculas com a última letra em minúscula.
string = input('Digite uma string: ')
print(string.upper().capitalize())

# 23. Receba uma string do usuário e troque todas as letras "s" por "$".
string = input('Digite uma string: ')
print(string.replace('s', '$'))

# 24. Receba uma string do usuário e conte quantas vezes a palavra "exemplo" aparece.
string = input('Digite uma string: ')
print(string.count('exemplo'))

# 25. Receba uma string do usuário e substitua todas as letras "o" por "a".
string = input('Digite uma string: ')
print(string.replace('o', 'a'))

# 26. Receba uma string do usuário e remova todos os caracteres que não são letras nem números.
string = input('Digite uma string: ')
print(string.replace(' ', ''))

# 27. Receba uma string do usuário e exiba-a em letras minúsculas com a primeira letra em maiúscula.
string = input('Digite uma string: ')
print(string.lower().capitalize())

# 28. Receba uma string do usuário e remova todas as letras "r".
string = input('Digite uma string: ')
print(string.replace('r', ''))

# 29. Receba uma string do usuário e exiba-a em letras maiúsculas com todas as vogais em minúsculas.
string = input('Digite uma string: ')
print(string.upper().replace('A', 'a').replace('E', 'e').replace('I', 'i').replace('O', 'o').replace('U', 'u'))

# 30. Receba uma string do usuário e conte quantas vezes a letra "a" aparece.
string = input('Digite uma string: ')
print(string.count('a'))

# 31. Peça ao usuário para inserir um número inteiro e uma palavra. Repita a palavra o número de vezes indicado pelo usuário.
numero = int(input('Digite um número: '))
palavra = input('Digite uma palavra: ')
print(palavra * numero)

# 32. Peça ao usuário para inserir um número e uma palavra. Imprima a palavra concatenada com o número sem espaço.
numero = int(input('Digite um número: '))
palavra = input('Digite uma palavra: ')
print(palavra + str(numero))

# 33. Peça ao usuário para inserir uma frase longa. Imprima a frase com todas as vogais substituídas por asteriscos.
frase = input('Digite uma frase: ')
print(frase.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*'))

# 34. Receba um número do usuário e calcule a raiz quadrada dele, arredondando o resultado para duas casas decimais.
numero = float(input('Digite um número: '))
print(round(numero ** 0.5, 2))

# 35. Receba dois números do usuário e calcule a potência do primeiro elevado ao segundo, arredondando o resultado para duas casas decimais.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(round(numero1 ** numero2, 2))

# 36. Receba um número do usuário e calcule o logaritmo natural desse número, arredondando o resultado para duas casas decimais.
numero = float(input('Digite um número: '))
print(round(math.log(numero), 2))

# 37. Receba um número do usuário e calcule o seu valor absoluto.
numero = float(input('Digite um número: '))
print(abs(numero))

# 38. Receba dois números do usuário e calcule o quociente e o resto da divisão do primeiro pelo segundo, respectivamente.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print('o quociente é {}'.format(numero1 // numero2))
print('o resto é {}'.format(numero1 % numero2))

# 39. Receba um número do usuário e calcule o seu fatorial.
numero = int(input('Digite um número: '))
print(math.factorial(numero))

# 40. Receba um número do usuário e calcule o seu arredondamento para baixo e para cima, respectivamente.
numero = float(input('Digite um número: '))
print(math.floor(numero))
print(math.ceil(numero))

# 41. Receba dois números do usuário e calcule a potência do primeiro elevado ao segundo, arredondando o resultado para baixo e para cima, respectivamente.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(math.floor(numero1 ** numero2))
print(math.ceil(numero1 ** numero2))

# 42. Receba um número do usuário e calcule o seu valor absoluto e a sua raiz quadrada, respectivamente.
numero = float(input('Digite um número: '))
print(abs(numero))
print(numero ** 0.5)

# 43. Receba dois números do usuário e calcule o logaritmo natural do primeiro elevado ao segundo, arredondando o resultado para duas casas decimais.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(round(math.log(numero1 ** numero2), 2))

# 44. Receba dois números do usuário e calcule o valor absoluto da diferença entre eles.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(abs(numero1 - numero2))

# 45. Receba um número do usuário e calcule a sua raiz quadrada, arredondando o resultado para baixo e para cima, respectivamente.
numero = float(input('Digite um número: '))
print(math.floor(numero ** 0.5))
print(math.ceil(numero ** 0.5))

# 46. Receba um número do usuário e calcule o seu arredondamento para baixo e para cima, respectivamente. Em seguida, calcule a potência de 2 elevado a cada um desses valores arredondados.
numero = float(input('Digite um número: '))
print(math.floor(numero))
print(math.ceil(numero))
print(2 ** math.floor(numero))
print(2 ** math.ceil(numero))

# 47. Receba um número do usuário e calcule o logaritmo natural desse número, arredondando o resultado para baixo e para cima, respectivamente. Em seguida, calcule a potência de 2 elevado a cada um desses valores arredondados.
numero = float(input('Digite um número: '))
print(math.floor(math.log(numero)))
print(math.ceil(math.log(numero)))
print(2 ** math.floor(math.log(numero)))
print(2 ** math.ceil(math.log(numero)))

# 48. Receba dois números do usuário e calcule o logaritmo natural do primeiro elevado ao segundo, arredondando o resultado para baixo e para cima, respectivamente. Em seguida, calcule a potência de 2 elevado a cada um desses valores arredondados.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(math.floor(math.log(numero1 ** numero2)))
print(math.ceil(math.log(numero1 ** numero2)))
print(2 ** math.floor(math.log(numero1 ** numero2)))
print(2 ** math.ceil(math.log(numero1 ** numero2)))

# 49. Receba dois números do usuário e calcule o quociente e o resto da divisão do primeiro pelo segundo, respectivamente. Em seguida, calcule a raiz quadrada de cada um desses valores e some os resultados.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(math.sqrt(numero1 // numero2))
print(math.sqrt(numero1 % numero2))
print(math.sqrt(numero1 // numero2) + math.sqrt(numero1 % numero2))

# 50. Receba um número do usuário e calcule o seu fatorial. Em seguida, calcule o logaritmo natural desse valor, arredondando o resultado para baixo e para cima, respectivamente.
numero = int(input('Digite um número: '))
print(math.factorial(numero))
print(math.floor(math.log(math.factorial(numero))))
print(math.ceil(math.log(math.factorial(numero))))

# 51. Receba um número do usuário e calcule a sua raiz quadrada. Em seguida, calcule o valor absoluto da diferença entre esse valor e o valor da constante pi do módulo math.
numero = float(input('Digite um número: '))
print(math.sqrt(numero))
print(abs(math.sqrt(numero) - math.pi))

# 52. Receba dois números do usuário e calcule o arredondamento para baixo e para cima do primeiro, respectivamente. Em seguida, calcule a potência do segundo elevado a cada um desses valores arredondados e some os resultados.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(math.floor(numero1))
print(math.ceil(numero1))
print(numero2 ** math.floor(numero1))
print(numero2 ** math.ceil(numero1))
print(numero2 ** math.floor(numero1) + numero2 ** math.ceil(numero1))

# 53. Receba um número do usuário e calcule a sua raiz quadrada. Em seguida, calcule o valor absoluto da diferença entre esse valor e a constante de Euler do módulo math.
numero = float(input('Digite um número: '))
print(math.sqrt(numero))
print(abs(math.sqrt(numero) - math.e))

# 54. Receba dois números do usuário e calcule a potência do primeiro elevado ao segundo. Em seguida, calcule o valor absoluto da diferença entre esse resultado e a constante de Euler do módulo math.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(numero1 ** numero2)
print(abs(numero1 ** numero2 - math.e))

# 55. Receba um número do usuário e calcule o logaritmo natural desse número. Em seguida, calcule a raiz quadrada desse valor e multiplique pelo valor de pi do módulo math.
numero = float(input('Digite um número: '))
print(math.log(numero))
print(math.sqrt(math.log(numero)))
print(math.sqrt(math.log(numero)) * math.pi)

# 56. Receba dois números do usuário e calcule o quociente e o resto da divisão do primeiro pelo segundo, respectivamente. Em seguida, calcule a potência de 2 elevado ao quociente e multiplique pelo resto.
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(numero1 // numero2)
print(numero1 % numero2)
print(2 ** (numero1 // numero2))
print(2 ** (numero1 % numero2))
print(2 ** (numero1 // numero2) * (numero1 % numero2))

# 57. Receba um número do usuário e calcule a sua raiz quadrada. Em seguida, calcule o seu arredondamento para baixo e para cima, respectivamente. Em seguida, calcule o fatorial de cada um desses valores arredondados e some os resultados.
numero = float(input('Digite um número: '))
print(math.sqrt(numero))
print(math.floor(math.sqrt(numero)))
print(math.ceil(math.sqrt(numero)))
print(math.factorial(math.floor(math.sqrt(numero))))
print(math.factorial(math.ceil(math.sqrt(numero))))
print(math.factorial(math.floor(math.sqrt(numero))) + math.factorial(math.ceil(math.sqrt(numero))))

# 58. Receba do usuário o valor de um ângulo em graus e calcule o seno desse ângulo utilizando a função sin do módulo math
angulo = input('Digite um ângulo em graus: ')
print(math.sin(math.radians(angulo)))

# 59. Receba do usuário dois números inteiros e calcule o resultado da operação de divisão inteira utilizando a função divmod.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print(divmod(numero1, numero2))

# 60. Receba do usuário um número float e calcule a sua parte inteira utilizando a função floor do módulo math.
numero = float(input('Digite um número: '))
print(math.floor(numero))

# 61. Receba do usuário um número inteiro e calcule o seu fatorial utilizando a função factorial do módulo math.
numero = int(input('Digite um número: '))
print(math.factorial(numero))

# 62. Receba do usuário um número float e calcule o seu valor absoluto utilizando a função abs do módulo math.
numero = float(input('Digite um número: '))
print(math.fabs(numero))

# 63. Receba do usuário um número float e calcule a sua raiz quadrada utilizando a função sqrt do módulo math.
numero = float(input('Digite um número: '))
print(math.sqrt(numero))

# 64. Receba do usuário o valor do raio de um círculo e calcule a sua área utilizando a constante pi do módulo math.
raio = float(input('Digite o valor do raio de um círculo: '))
print(math.pi * raio ** 2)

# 65. Receba do usuário o valor de uma base e de um expoente e calcule a potência utilizando a função pow do módulo math.
base = float(input('Digite o valor da base: '))
expoente = float(input('Digite o valor do expoente: '))
print(math.pow(base, expoente))

# 66. Receba do usuário um número float e arredonde-o para cima utilizando a função ceil do módulo math.
numero = float(input('Digite um número: '))
print(math.ceil(numero))

# 67. Receba do usuário um número float e arredonde-o para baixo utilizando a função floor do módulo math.
numero = float(input('Digite um número: '))
print(math.floor(numero))

# 68. Receba do usuário dois números inteiros e calcule o máximo divisor comum utilizando a função gcd do módulo math.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print(math.gcd(numero1, numero2))

# 69. Receba do usuário o valor de um ângulo em graus e calcule o seu cosseno utilizando a função cos do módulo math.
angulo = float(input('Digite um ângulo em graus: '))
print(math.cos(math.radians(angulo)))

# 70. Receba do usuário um número float e calcule a sua parte decimal utilizando a função modf do módulo math.
numero = float(input('Digite um número: '))
print(math.modf(numero))

# 71. Receba do usuário um número float e calcule o seu logaritmo natural utilizando a função log do módulo math.
numero = float(input('Digite um número: '))
print(math.log(numero))

# 72. Receba do usuário dois números inteiros e calcule o mínimo múltiplo comum utilizando a função lcm do módulo math.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print(math.lcm(numero1, numero2))

# 73. Receba do usuário o valor de um ângulo em radianos e calcule a sua tangente utilizando a função tan do módulo math.
angulo = float(input('Digite um ângulo em radianos: '))
print(math.tan(angulo))

# 74. Receba do usuário um número float e calcule o seu arco tangente utilizando a função atan do módulo math.
numero = float(input('Digite um número: '))
print(math.atan(numero))

# 75. Receba do usuário dois números inteiros e calcule a potência modular utilizando a função pow do módulo math.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print(math.pow(numero1, numero2))

# 76. Receba do usuário um número float e calcule a sua exponencial utilizando a função exp do módulo math.
numero = float(input('Digite um número: '))
print(math.exp(numero))
