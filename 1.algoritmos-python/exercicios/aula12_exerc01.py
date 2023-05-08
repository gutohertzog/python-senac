# ---------------------------------- AULA 12 ----------------------------------
# ---------------------------------- EXER 01 ----------------------------------
# Crie um algoritmo que crie uma lista de 100 números aleatórios entre -10.000 e 10.000. Sem ordenar a lista, separe todos os números dela em listas menores de:
# a. Zeros;
# b. Pares;
# c. Ímpares;
# d. Positivos;
# e. Negativos;
# f. Múltiplos de 3;
# g. Múltiplos de 5;
# h. Múltiplos de 7;
# i. Múltiplos de 3 e 5;
# j. Múltiplos de 3 e 7;
# k. Múltiplos de 5 e 7;
# l. Múltiplos de 3, 5 e 7;
# m. Números que não se encaixaram em nenhum dos critérios acima;
# Ao final do algoritmo, mostre o tamanho das 13 listas e seus respectivos valores. Caso alguma lista tenha ficado vazia, mostre uma mensagem informando ao usuário.

import random

lista = []
lista_zeros = []
lista_pares = []
lista_impares = []
lista_positivos = []
lista_negativos = []
lista_mult3 = []
lista_mult5 = []
lista_mult7 = []
lista_mult3e5 = []
lista_mult3e7 = []
lista_mult5e7 = []
lista_mult3e5e7 = []
lista_nao_se_encaixaram = []

for i in range(100):
    lista.append(random.randint(-10000, 10000))

for i in lista:
    if i == 0:
        lista_zeros.append(i)
    elif i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

    if i > 0:
        lista_positivos.append(i)
    else:
        lista_negativos.append(i)

    if i % 3 == 0:
        lista_mult3.append(i)
    if i % 5 == 0:
        lista_mult5.append(i)
    if i % 7 == 0:
        lista_mult7.append(i)
    if i % 3 == 0 and i % 5 == 0:
        lista_mult3e5.append(i)
    if i % 3 == 0 and i % 7 == 0:
        lista_mult3e7.append(i)
    if i % 5 == 0 and i % 7 == 0:
        lista_mult5e7.append(i)
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        lista_mult3e5e7.append(i)
    # para tornar este filtro ativo, ele vai receber os números não múltiplos
    # de 3, 5 e 7
    if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        lista_nao_se_encaixaram.append(i)

print(f'Lista: {lista}')
print(f'Lista de zeros: {lista_zeros}')
print(f'Lista de pares: {lista_pares}')
print(f'Lista de ímpares: {lista_impares}')
print(f'Lista de positivos: {lista_positivos}')
print(f'Lista de negativos: {lista_negativos}')
print(f'Lista de múltiplos de 3: {lista_mult3}')
print(f'Lista de múltiplos de 5: {lista_mult5}')
print(f'Lista de múltiplos de 7: {lista_mult7}')
print(f'Lista de múltiplos de 3 e 5: {lista_mult3e5}')
print(f'Lista de múltiplos de 3 e 7: {lista_mult3e7}')
print(f'Lista de múltiplos de 5 e 7: {lista_mult5e7}')
print(f'Lista de múltiplos de 3, 5 e 7: {lista_mult3e5e7}')
print(
    f'Lista de números que não se encaixaram em nenhum dos critérios acima: {lista_nao_se_encaixaram}')

print(f'\nTamanho da lista: {len(lista)}')
print(f'Tamanho da lista de zeros: {len(lista_zeros)}')
print(f'Tamanho da lista de pares: {len(lista_pares)}')
print(f'Tamanho da lista de ímpares: {len(lista_impares)}')
print(f'Tamanho da lista de positivos: {len(lista_positivos)}')
print(f'Tamanho da lista de negativos: {len(lista_negativos)}')
print(f'Tamanho da lista de múltiplos de 3: {len(lista_mult3)}')
print(f'Tamanho da lista de múltiplos de 5: {len(lista_mult5)}')
print(f'Tamanho da lista de múltiplos de 7: {len(lista_mult7)}')
print(f'Tamanho da lista de múltiplos de 3 e 5: {len(lista_mult3e5)}')
print(f'Tamanho da lista de múltiplos de 3 e 7: {len(lista_mult3e7)}')
print(f'Tamanho da lista de múltiplos de 5 e 7: {len(lista_mult5e7)}')
print(f'Tamanho da lista de múltiplos de 3, 5 e 7: {len(lista_mult3e5e7)}')
print(
    f'Tamanho da lista de números que não se encaixaram em nenhum dos critérios acima: {len(lista_nao_se_encaixaram)}')
