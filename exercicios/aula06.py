# 1. Faça um programa que leia dois números inteiros e verifique se o primeiro é maior que o segundo.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
else:
    print('{} não é maior que {}'.format(num1, num2))

# 2. Crie um programa que leia um número inteiro e verifique se ele é par ou ímpar.
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('{} é par'.format(num))
else:
    print('{} é ímpar'.format(num))

# 3. Escreva um programa que leia um número e verifique se ele é positivo, negativo ou zero.
num = int(input('Digite um número: '))
if num > 0:
    print('{} é positivo'.format(num))
elif num < 0:
    print('{} é negativo'.format(num))
else:
    print('{} é zero'.format(num))

# 4. Crie um programa que leia um número inteiro e verifique se ele é um múltiplo de 3.
num = int(input('Digite um número: '))
if num % 3 == 0:
    print('{} é múltiplo de 3'.format(num))
else:
    print('{} não é múltiplo de 3'.format(num))

# 5. Escreva um programa que leia a idade de uma pessoa e exiba se ela é maior de idade ou não.
idade = int(input('Digite a idade: '))
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

# 6. Faça um programa que leia dois números e exiba o resultado da soma se os números forem iguais, e o resultado da multiplicação se eles forem diferentes.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 == num2:
    print('Soma: {}'.format(num1 + num2))
else:
    print('Multiplicação: {}'.format(num1 * num2))

# 7. Escreva um programa que leia um número inteiro e exiba o seu valor absoluto.
num = int(input('Digite um número: '))
if num < 0:
    num = num * -1
print('Valor absoluto: {}'.format(num))

# 8. Faça um programa que leia três notas de um aluno e calcule a média. Se a média for maior ou igual a 7, exiba "Aprovado", senão exiba "Reprovado".
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

# 9. Crie um programa que leia um número inteiro e verifique se ele é divisível por 5 ou por 6.
num = int(input('Digite um número: '))
if num % 5 == 0:
    print('{} é divisível por 5'.format(num))
elif num % 6 == 0:
    print('{} é divisível por 6'.format(num))
else:
    print('{} não é divisível por 5 ou por 6'.format(num))

# 10. Escreva um programa que leia o peso e a altura de uma pessoa e exiba o seu índice de massa corporal (IMC). Se o IMC for menor que 18.5, exiba "Abaixo do peso". Se o IMC estiver entre 18.5 e 24.9, exiba "Peso normal". Se o IMC estiver entre 25 e 29.9, exiba "Sobrepeso". Se o IMC estiver entre 30 e 34.9, exiba "Obesidade grau I". Se o IMC estiver entre 35 e 39.9, exiba "Obesidade grau II". Se o IMC for maior ou igual a 40, exiba "Obesidade grau III".
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade grau I')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')

# 11. Faça um programa que leia um número inteiro e verifique se ele é par e positivo.
num = int(input('Digite um número: '))
if num % 2 == 0 and num > 0:
    print('{} é par e positivo'.format(num))
else:
    print('{} não é par e positivo'.format(num))

# 12. Crie um programa que leia o salário de um funcionário e exiba o seu novo salário, considerando um aumento de 15% se o salário for menor ou igual a R$ 1.500,00 e um aumento de 10% se o salário for maior que R$ 1.500,00.
salario = float(input('Digite o salário: '))
if salario <= 1500:
    salario = salario * 1.15
else:
    salario = salario * 1.10
print('Novo salário: {}'.format(salario))

# 13. Escreva um programa que leia um número inteiro e verifique se ele é divisível por 2 e por 3.
num = int(input('Digite um número: '))
if num % 2 == 0 and num % 3 == 0:
    print('{} é divisível por 2 e por 3'.format(num))
else:
    print('{} não é divisível por 2 e por 3'.format(num))

# 14. Faça um programa que leia dois números e exiba o resultado da divisão do primeiro pelo segundo. Se o segundo número for igual a zero, exiba "Não é possível dividir por zero".
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num2 == 0:
    print('Não é possível dividir por zero')
else:
    print('Resultado da divisão: {}'.format(num1 / num2))

# 15. Crie um programa que leia um número inteiro e verifique se ele é positivo e ímpar.
num = int(input('Digite um número: '))
if num > 0 and num % 2 != 0:
    print('{} é positivo e ímpar'.format(num))
else:
    print('{} não é positivo e ímpar'.format(num))

# 16. Escreva um programa que leia um número inteiro e verifique se ele é maior que 100 ou menor que -100.
num = int(input('Digite um número: '))
if num > 100 or num < -100:
    print('{} é maior que 100 ou menor que -100'.format(num))
else:
    print('{} não é maior que 100 ou menor que -100'.format(num))

# 17. Faça um programa que leia a idade de uma pessoa e exiba se ela é criança (até 12 anos), adolescente (de 13 a 17 anos), adulto (de 18 a 59 anos) ou idoso (a partir dos 60 anos).
idade = int(input('Digite a idade: '))
if idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 17:
    print('Adolescente')
elif idade >= 18 and idade <= 59:
    print('Adulto')
else:
    print('Idoso')

# 18. Faça um programa que receba a idade de uma pessoa e sua altura em metros. Caso a idade seja maior que 18 anos e a altura seja maior ou igual a 1.70m, exiba "Você pode entrar no brinquedo". Caso contrário, exiba "Você não pode entrar no brinquedo".
idade = int(input('Digite a idade: '))
altura = float(input('Digite a altura: '))
if idade > 18 and altura >= 1.70:
    print('Você pode entrar no brinquedo')
else:
    print('Você não pode entrar no brinquedo')

# 19. Escreva um programa que leia dois valores numéricos e exiba qual deles é o maior. Caso os valores sejam iguais, exiba "Os valores são iguais".
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num2, num1))
else:
    print('Os valores são iguais')

# 20. Crie um programa que leia três números e exiba-os em ordem crescente e em ordem decrescente.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print('Ordem crescente: {}, {}, {}'.format(num3, num2, num1))
        print('Ordem decrescente: {}, {}, {}'.format(num1, num2, num3))
    else:
        print('Ordem crescente: {}, {}, {}'.format(num2, num3, num1))
        print('Ordem decrescente: {}, {}, {}'.format(num1, num3, num2))
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print('Ordem crescente: {}, {}, {}'.format(num3, num1, num2))
        print('Ordem decrescente: {}, {}, {}'.format(num2, num1, num3))
    else:
        print('Ordem crescente: {}, {}, {}'.format(num1, num3, num2))
        print('Ordem decrescente: {}, {}, {}'.format(num2, num3, num1))
else:
    if num1 > num2:
        print('Ordem crescente: {}, {}, {}'.format(num2, num1, num3))
        print('Ordem decrescente: {}, {}, {}'.format(num3, num1, num2))
    else:
        print('Ordem crescente: {}, {}, {}'.format(num1, num2, num3))
        print('Ordem decrescente: {}, {}, {}'.format(num3, num2, num1))

# 21. Crie um programa que leia uma letra do alfabeto e verifique se ela é uma vogal ou uma consoante. Caso seja uma vogal, exiba "A letra é uma vogal". Caso seja uma consoante, exiba "A letra é uma consoante".
letra = input('Digite uma letra: ')
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('A letra é uma vogal')
else:
    print('A letra é uma consoante')

# 22. Escreva um programa que leia uma temperatura em graus Celsius e a converta para graus Fahrenheit. Caso a temperatura em Celsius seja menor que -273.15, exiba "Temperatura inválida".
celsius = float(input('Digite a temperatura em Celsius: '))
if celsius < -273.15:
    print('Temperatura inválida')
else:
    fahrenheit = (celsius * 9 / 5) + 32
    print('Temperatura em Fahrenheit: {}'.format(fahrenheit))

# 23. Crie um programa que leia um número inteiro e verifique se ele é positivo, negativo ou zero. Caso seja positivo, exiba "O número é positivo". Caso seja negativo, exiba "O número é negativo". Caso seja zero, exiba "O número é zero".
num = int(input('Digite um número: '))
if num > 0:
    print('O número é positivo')
elif num < 0:
    print('O número é negativo')
else:
    print('O número é zero')

# 24. Faça um programa que leia um número inteiro e exiba a sua tabuada de multiplicação, do 1 até o 10.
num = int(input('Digite um número: '))
print('{} x 1 = {}'.format(num, num * 1))
print('{} x 2 = {}'.format(num, num * 2))
print('{} x 3 = {}'.format(num, num * 3))
print('{} x 4 = {}'.format(num, num * 4))
print('{} x 5 = {}'.format(num, num * 5))
print('{} x 6 = {}'.format(num, num * 6))
print('{} x 7 = {}'.format(num, num * 7))
print('{} x 8 = {}'.format(num, num * 8))
print('{} x 9 = {}'.format(num, num * 9))

# 25. Escreva um programa que leia três valores numéricos e exiba a média aritmética dos três. Caso a média seja maior ou igual a 7, exiba "Aprovado". Caso contrário, exiba "Reprovado".
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
media = (num1 + num2 + num3) / 3
if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

# 26. Crie um programa que leia o ano atual e o ano de nascimento de uma pessoa. O programa deve calcular a idade da pessoa e verificar em qual faixa etária ela se encaixa: criança (até 12 anos), adolescente (entre 13 e 17 anos), adulto (entre 18 e 59 anos) ou idoso (a partir dos 60 anos). Exiba a faixa etária correspondente.
ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')

# 27. Crie um programa que leia um número inteiro e verifique se ele é positivo e par. Caso seja positivo e par, exiba "O número é positivo e par". Caso contrário, exiba "O número não é positivo e par".
num = int(input('Digite um número: '))
if num > 0 and num % 2 == 0:
    print('O número é positivo e par')
else:
    print('O número não é positivo e par')

# 28. Escreva um programa que leia três valores numéricos e exiba a média ponderada dos três. Para calcular a média ponderada, utilize os pesos 2, 3 e 5, respectivamente.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
media = (num1 * 2 + num2 * 3 + num3 * 5) / 10
print('Média ponderada: {}'.format(media))

# 29. Faça um programa que leia o nome, o sexo e a idade de uma pessoa. Caso a pessoa seja do sexo masculino e tenha idade entre 18 e 25 anos, exiba "Você foi selecionado para o alistamento". Caso contrário, exiba "Infelizmente você não foi selecionado para o alistamento".
nome = input('Digite o nome: ')
sexo = input('Digite o sexo: ')
idade = int(input('Digite a idade: '))
if sexo == 'masculino' and idade >= 18 and idade <= 25:
    print('Você foi selecionado para o alistamento')
else:
    print('Infelizmente você não foi selecionado para o alistamento')
