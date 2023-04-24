# ---------------------------------- AULA 08 ----------------------------------
# ---------------------------------- EXER 01 ----------------------------------
# Faça um programa que leia um número inteiro e exiba a soma dos seus dígitos.
# Exemplo: 486 vai gerar 4+8+6 = 18.

digitos = input('Digite um número inteiro positivo qualquer : ')

# método 1
# soma é uma variável que vai receber o valor 0
soma = 0
# para cada letra em digitos faça
for letra in digitos:
    # soma recebe soma + letra convertida para inteiro
    soma = soma + int(letra)
# imprime a soma
print('A soma é :', soma)

# método 2
# Este código soma os digitos do número fornecido pelo usuário
# A variável soma é inicializada com zero
soma = 0
# A variável digitos recebe o valor fornecido pelo usuário
digitos = int(digitos)
# Enquanto digitos for maior que zero, o código continua
while digitos > 0:
    # O código pega o último digito do número
    digito = digitos % 10
    # O código soma o último digito ao valor da variável soma
    soma += digito
    # O código divide o valor da variável digitos por 10
    digitos //= 10
    # O código retorna ao laço while até que a condição seja falsa
# O código imprime na tela o valor da variável soma
print('A soma é :', soma)
