# ---------------------------------- AULA 08 ----------------------------------
# ---------------------------------- EXER 01 ----------------------------------
# Faça um programa que leia um número inteiro e exiba a soma dos seus dígitos.
# Exemplo: 486 vai gerar 4+8+6 = 18.

digitos = input('Digite um número inteiro positivo qualquer : ')

soma = 0
for letra in digitos:
    soma = soma + int(letra)
print('A soma é : ', soma)
