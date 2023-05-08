# ---------------------------------- AULA 06 ----------------------------------
# ---------------------------------- EXER 01 ----------------------------------
# Faça um programa que leia três números e exiba o maior deles.

# pega os números do usuário e os converte para float
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# método 1
if num1 > num2:
    if num1 > num3:
        maior = num1
        if num2 > num3:
            meio = num2
            menor = num3
        else:
            meio = num3
            menor = num2
    else:
        maior = num3
        meio = num1
        menor = num2
else:
    if num2 > num3:
        maior = num2
        if num1 > num3:
            meio = num1
            menor = num3
        else:
            meio = num3
            menor = num1
    else:
        maior = num3
        meio = num2
        menor = num1

print("Ordem crescente: ", menor, ",", meio, ",", maior)
print("Ordem decrescente: ", maior, ",", meio, ",", menor)

# método 2
if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num3:
        meio = num2
        menor = num3
    else:
        meio = num3
        menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2
    if num1 > num3:
        meio = num1
        menor = num3
    else:
        meio = num3
        menor = num1
else:
    maior = num3
    if num1 > num2:
        meio = num1
        menor = num2
    else:
        meio = num2
        menor = num1

print("Ordem crescente: ", menor, ",", meio, ",", maior)
print("Ordem decrescente: ", maior, ",", meio, ",", menor)

# método 3
# este método apenas busca o maior dos valores
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print('O maior é', maior)

# método 4
# este método realiza todas as comparações possíveis
if num1 > num2 and num1 > num3:
    print("O maior número é: ",num1)
elif num2 > num1 and num2 > num3:
    print("O maior número é: ",num2)
elif num3 > num1 and num3 > num2:
    print("O maior número é: ",num3)

# método 5
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

print("O maior número é:", maior)
